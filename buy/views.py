from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.core.paginator import Paginator
from django.views import generic
from django.db.models import Exists, Q
from trade.models import Estimate, Bid
from .forms import EstimateForm

# urls.py에서 name='함수이름'일 때(=주소/buy/'' 일 때), 함수가 실행됩니다.
# 버튼 연결과는 무관하게 url입력해서 들어가는 액션입니다.

# p05 (buy/main/)
def main(request):
    return render(request, 'common/temp/05_메인(로그인전).html')

# buy/estimates
def estimate_list(request):
    page = request.GET.get('page', '1')  # 페이지
    own_estimate_list = Estimate.objects.filter(buyer_id=request.user)
    # Bid에서 낙찰하지 않은 것만 보여준다.
    finished_bid = Bid.objects.filter(
        estimate_id__in=own_estimate_list,
        finished=True
    )
    cannot_bid_estimates = [bid.estimate_id.pk for bid in finished_bid]
    # 낙찰된 품목을 제외하고 등록된 견적들을 조회.
    own_estimate_list = own_estimate_list.filter(~Q(estimate_id__in=cannot_bid_estimates)) 
    
    paginator = Paginator(own_estimate_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'estimate_list': page_obj}
    return render(request, 'buyer/temp/19_구매견적요청메인(등록완료).html', context)

# buy/estimates/<estimate_id> -- ex) buy/estimates/f52f1eb8-6b49-4b56-964b-7f9516844ee2
def estimate_detail(request, estimate_id):
    bid = Bid.objects.filter(estimate_id= estimate_id)
    context = {
        'bids': bid,
        'bid_count': bid.count
        }
    return render(request, 'buyer/temp/23_구매입찰업체현황.html', context)

# buy/register
def register_estimate(request):
    if request.method == 'POST':
        form = EstimateForm(request.POST, request.FILES)
        details = request.POST.getlist('detail')
        details_for_DB = "/".join(details)

        if form.is_valid():
            estimate = form.save(commit=False)
            estimate.reg_date = timezone.now()
            estimate.buyer_id = request.user
            estimate.detail = details_for_DB
            estimate.save()
            return redirect('buy:estimate_list')
    else:
        form = EstimateForm()
    return render(request, 'buyer/temp/18_구매견적요청상세.html', { 'form': form })
