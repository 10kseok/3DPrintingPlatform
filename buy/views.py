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

# p16 (buy/1/)
def index1(request):
    estimate_list = Estimate.objects.order_by('-reg_date')
    context = {'estimate_list': estimate_list}
    return render(request, 'buyer/temp/16_구매견적요청메인(등록전).html', context)

#p19 (buy/2/)
def index2(request):
    estimate_list = Estimate.objects.order_by('-reg_date')
    context = {'estimate_list': estimate_list}
    return render(request, 'buyer/temp/19_구매견적요청메인(등록완료).html', context)

# p18 (buy/ing/)
def estimating(request):
    return render(request, 'buyer/temp/18_구매견적요청상세.html')

# p23 (buy/detail/)
def estimate_detail(request):
    return render(request, 'buyer/temp/23_구매입찰업체현황.html')

# p13 (buy/sign_up/)
def sign_up(request):
    return render(request, 'common/temp/13_회원가입(의뢰인).html')

# p12 (buy/position_choice/)
def position_choice(request):
    return render(request, 'common/temp/12_회원가입(포지션선택).html')

# p07 (buy/sign_in/)
def sign_in(request):
    return render(request, 'common/temp/07_로그인.html')

# p05 (buy/main/)
def main(request):
    return render(request, 'common/temp/05_메인(로그인전).html')
    
##################################################################
def buyer_estimate_list(request):
    page = request.GET.get('page', '1')  # 페이지
    estimate_list = Estimate.objects.filter(buyer_id= request.user).order_by('-reg_date')
    paginator = Paginator(estimate_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'estimate_list': page_obj}
    return render(request, 'buyer/temp/19_구매견적요청메인(등록완료).html', context)


def buyer_estimate_detail(request, estimate_id):
    bid = Bid.objects.filter(estimate_id= estimate_id)
    context = {'bids': bid}
    return render(request, 'buyer/temp/23_구매입찰업체현황.html', context)


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
            #return redirect('buy:buyer_estimate_list')
            return redirect('buy:index2')
    else:
        form = EstimateForm()
    return render(request, 'buyer/temp/18_구매견적요청상세.html', { 'form': form })
