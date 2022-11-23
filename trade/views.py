from django.shortcuts import render
from .models import Estimate, Bid, Trade
from common.models import User
from django.utils import timezone

def buy_complete(request, bid_id):
    # TODO: 
    # 1. Bid 정보, Estimate 정보 받아옴
    bid = Bid.objects.get(pk=bid_id)
    estimate = bid.estimate_id
    # 2. 해당 bid 낙찰 (상태변경)
    bid.finished = True
    estimate.canBid = False
    # 3. Trade 생성
    trade = Trade(
        estimate_id= bid.estimate_id,
        bid_id= bid,
        success_date= timezone.now(),
        product_state= "PROCESSING"
    )

    try:
        # 이미 존재하는 거래 데이터를 생성하려고 할 때 
        isExistTrade = Trade.objects.get(estimate_id=bid.estimate_id)
    except:
        # 정상적인 거래시 모든 데이터들 저장
        trade.save()
        estimate.save()
        bid.save()

    seller_info = User.objects.get(username= bid.seller_id) 
    return render(request, 'trade/temp/34_구매거래완료.html',
                {   
                    'trade': trade,
                    'estimate': estimate,
                    'bid': bid,
                    'seller_info': seller_info,
                }
            )
    
def sell_complete(request, bid_id):
    trade = Trade.objects.get(bid_id=bid_id)
    bid = trade.bid_id
    estimate = trade.estimate_id
    
    return render(request, 'trade/temp/35_판매거래완료.html',
                { 
                    'trade': trade,
                    'bid': bid,
                    'estimate': estimate,
                }
            )