from django.shortcuts import render
from .models import Estimate, Bid, Trade


def buy_complete(request):
    return render(request, 'trade/temp/34_구매거래완료.html')
def sell_complete(request):
    return render(request, 'trade/temp/35_판매거래완료.html')