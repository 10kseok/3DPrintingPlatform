from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.core.paginator import Paginator
from django.views import generic
from django.db.models import Exists, Q
from trade.models import Estimate
from .forms import EstimateForm

# urls.py에서 name=index일 때(=주소/buy 일 때), index함수가 실행됩니다.
def index(request):
    estimate_list = Estimate.objects.order_by('-reg_date')
    context = {'estimate_list': estimate_list}
    return render(request, 'buyer/temp/16_구매견적요청메인(등록전).html', context)
"""
def estimating(request, estimate_id):
    estimate = get_object_or_404(Estimate, pk=estimate_id)
    context = {'estimate': estimate}
    return render(request, 'buyer/temp/18_구매견적요청상세.html', context)
"""
def detail(request, estimate_id):
    estimate = get_object_or_404(Estimate, pk=estimate_id)
    context = {'estimate': estimate}
    return render(request, 'temp_detail.html', context)

def buyer_estimate_list(request):
    page = request.GET.get('page', '1')  # 페이지
    estimate_list = Estimate.objects.order_by('-reg_date')
    paginator = Paginator(estimate_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'estimate_list': page_obj}
    return render(request, 'buyer_estimate_list.html', context)


def buyer_estimate_detail(request, estimate_id):
    estimate = get_object_or_404(Estimate, pk=estimate_id)
    context = {'estimate': estimate}
    return render(request, 'buyer_estimate_detail.html', context)


def buyer_estimate_form(request):
    if request.method == 'POST':
        form = EstimateForm(request.POST)
        if form.is_valid():
            estimate = form.save(commit=False)
            #question.author = request.user  # author 속성에 로그인 계정 저장
            estimate.reg_date = timezone.now()
            estimate.save()
            #return redirect('buy:buyer_estimate_list')
            return redirect('buyer/temp/16_구매견적요청메인(등록전).html')
    else:
        form = EstimateForm()
    context = {'form': form}
    #return render(request, 'buy:buyer_estimate_form.html', context)
    return render(request, 'buyer/temp/18_구매견적요청상세.html', context)