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
    bidding = Bid.objects.filter(finished=False, seller_id=temp_seller_id)
    completed = Bid.objects.filter(finished=True)
    
    context = {
        "estimates": estimates_before_bidding,
        "bidding": bidding,
        "completed": completed,
    }
    return render(request, "../templates/seller_kanban.html", context)

def estimate_detail(request, estimate_id):
    return render(request, "../templates/bid_estimate_detail.html")