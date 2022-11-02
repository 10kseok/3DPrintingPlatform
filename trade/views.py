from django.shortcuts import render
from .models import Estimate, Bid, Trade


def index(request):
    estimate = Estimate.objects.filter(project_name='짱구')
    bid = Bid.objects.filter(finished=False)
    # trade = Trade.objects.filter(product_state=1)
    trade = Trade.objects.all()
    context = {'estimate': estimate, 'bid': bid, 'trade': trade}
    return render(request, 'trade/35_판매거래완료.html', context)
