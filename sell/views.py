from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.db.models import Exists, Q
from trade.models import Estimate, Bid
# Create your views here.

def seller_kanban(request):
    temp_seller_id = "bluedragon"
    
    not_finished_bid = Bid.objects.filter(finished=True).values('estimate_id')
    estimates_before_bidding = Estimate.objects.filter(
        ~Q(estimate_id__in = [item['estimate_id'] for item in not_finished_bid])
        )
    bidding = Bid.objects.filter(finished=False)
    completed = Bid.objects.filter(finished=True)
    
    context = {
        "estimates": estimates_before_bidding,
        "bidding": bidding,
        "completed": completed,
    }
    return render(request, "../templates/seller_kanban.html", context)

def estimate_detail(request, estimate_id):
    return render(request, "../templates/bid_estimate_detail.html")

# p35 (sell/complete/)
def complete(request):
    return render(request, 'trade/temp/35_판매거래완료.html')

# p28 (sell/kanban/)
def kanban(request):
    return render(request, 'seller/temp/seller_kanban.html')
    
# p29 (sell/detail/)
def detail(request):
    return render(request, 'seller/temp/29_판매경매품목상세.html')

# p14 (sell/sign_up/)
def sign_up(request):
    return render(request, 'common/temp/14_회원가입(생산자).html')