from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.db.models import Q
from trade.models import Estimate, Bid
from sell.models import Equipment
from django.utils import timezone
# Create your views here.

def bid_board(request):
    # 1. 보유한 장비목록 가져오기
    equipment = Equipment.objects.get(pk=request.user.equipment_id1)
    available_material = equipment.material.split("/") + ["NULL"]
    # 2. 제작가능한 estimate 조회
    available_estimates = Estimate.objects.filter(
        method__in=[equipment.method, "NULL"],
        material__in=available_material,
    )
    # 3. 자신이 입찰 넣은 bid 조회
    bidding = Bid.objects.filter(finished=False, seller_id=request.user)
    # 4. 낙찰된 건 조회
    completed_bid = Bid.objects.filter(finished=True, seller_id=request.user)
    # 넘겨줄 데이터
    context = {
        "estimates": available_estimates,
        "bidding": bidding,
        "completed": completed_bid,
    }
    return render(request, "seller/temp/bid_board.html", context)

def estimate_detail(request, estimate_id):
    estimate = Estimate.objects.get(pk=estimate_id)
    # 가격 제안시
    if request.method == 'POST':
        # Bid 데이터 생성
        bid = Bid(
            seller_id=request.user,
            estimate_id=estimate,
            price=int(request.POST.get('price')),
            bid_date=timezone.now(),
            finished=False
        )
        bid.save()
        return redirect('sell:bid_board')
    
    return render(request, "seller/temp/29_판매경매품목상세.html", { "estimate": estimate })
    
# p29 (sell/detail/)
def detail(request):
    return render(request, 'seller/temp/29_판매경매품목상세.html')