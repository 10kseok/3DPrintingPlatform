from django.shortcuts import render
from .models import Estimate, Bid, Trade


def estimate(request):
    estimate = Estimate.objects.filter(project_name='짱구')
    context = {'estimate': estimate}
    return render(request, 'trade/34_구매거래완료.html', context)

def bid(request):
    bid = Bid.objects.filter(finished=False)
    context = {'bid': bid}
    return render(request, 'trade/34_구매거래완료.html', context)

def trade(request):
    trade = Trade.objects.filter(product_state=1)
    context = {'trade': trade}
    return render(request, 'trade/34_구매거래완료.html', context)
# Create your views here.
