from django.shortcuts import render
from .models import Estimate, Bid, Trade
from common.models import User
from django.utils import timezone

def buy_complete(request, bid_id):
    # TODO: 
    # 1. bid 정보 받아옴
    bid = Bid.objects.get(pk= bid_id)
    # 2. 해당 bid 낙찰 (상태변경)
    bid.finished = True
    # 3. Trade 생성
    trade = Trade(
        estimate_id= bid.estimate_id,
        bid_id= bid,
        success_date= timezone.now(),
        product_state= "PROCESSING"
    )
    # NOTE: 실제 상세보기에서 판매자 선택버튼이 다 구현되면 주석해제
    # trade.save()
    estimate = Estimate.objects.get(pk= bid.estimate_id.pk)
    seller_info = User.objects.get(username= bid.seller_id) 
    return render(request, 'trade/temp/34_구매거래완료.html',
                {   
                    'trade': trade,
                    'estimate': estimate,
                    'bid': bid,
                    'seller_info': seller_info,
                }
            )
    

def sell_complete(request):
    return render(request, 'trade/temp/35_판매거래완료.html')