from django import template
from trade.models import Bid, Estimate
register = template.Library()

@register.filter
def getBidCount(estimate_id):
    '''
    Estimate_id에 맞는 Bid(입찰수) 개수 반환
    '''
    estimate_instance = Estimate.objects.get(estimate_id=estimate_id)
    bid_count = len(Bid.objects.filter(estimate_id=estimate_instance))

    return bid_count