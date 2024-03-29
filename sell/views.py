from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.db.models import Q
from trade.models import Estimate, Bid, Trade
from sell.models import Equipment
from django.utils import timezone
# Create your views here.

def bid_board(request):
    # 1. 보유한 장비목록 가져오기
    equipment = Equipment.objects.get(pk=request.user.equipment_id1)
    available_material = equipment.material.split("/") + ["상관없음"]
    # 2. 제작가능한 estimate 조회
    available_estimates = Estimate.objects.filter(
        method__in=[equipment.method, "상관없음"],
        material__in=available_material,
        canBid=True,
    ).order_by('-reg_date')
    # 3. 자신이 입찰 넣은 bid 조회
    bidding = Bid.objects.filter(finished=False, seller_id=request.user).order_by('-bid_date')
    # 3 - 1 자신이 입찰 넣은 Estimate는 available_material에서 제외
    available_estimates = available_estimates.filter(~Q(estimate_id__in=[bid.estimate_id.estimate_id for bid in bidding]))
    # 4. 낙찰된 건 조회
    completed_bid = Bid.objects.filter(finished=True, seller_id=request.user)
    trade = Trade.objects.filter(bid_id__in=completed_bid).order_by('-success_date')
    # 넘겨줄 데이터
    context = {
        "estimates": available_estimates,
        "bidding": bidding,
        "trade": trade,
    }
    return render(request, "seller/temp/bid_board.html", context)

def estimate_detail(request, estimate_id):
    estimate = Estimate.objects.get(pk=estimate_id)
    try:
        # 입찰한 내역이 있을 때(견적 수정)
        Bid.objects.get(seller_id=request.user, estimate_id=estimate)
        isUpdate = True
    except:
        # 새로운 입찰일 때(견적 제시)
        isUpdate = False

    if request.method == 'POST':
        # Bid 업데이트
        try:
            bid = Bid.objects.get(seller_id=request.user, estimate_id=estimate)
            bid.price = int(request.POST.get('price'))
            bid.bid_date = timezone.now()
        except:
        # Bid 데이터 첫 생성
            bid = Bid(
                seller_id=request.user,
                estimate_id=estimate,
                price=int(request.POST.get('price')),
                bid_date=timezone.now(),
                finished=False
            )
        bid.save()
        return redirect('sell:bid_board')
    
    return render(request, "seller/temp/29_판매경매품목상세.html", { "estimate": estimate, "isUpdate": isUpdate })
    
# p29 (sell/detail/)
def detail(request):
    return render(request, 'seller/temp/29_판매경매품목상세.html')