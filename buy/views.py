from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
#from trade.models import Estimate
from .models import Estimate
from .forms import EstimateForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# 구매자기본화면
def index(request):
    page = request.GET.get('page', '1')  # 페이지
    estimate_list = Estimate.objects.order_by('-reg_date')  # 등록일순 정렬
    paginator = Paginator(estimate_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'estimate_list': page_obj}
    return render(request, 'estimate/estimate_list.html', context)

# 견적상세화면
def detail(request, estimate_id):
    estimate = get_object_or_404(Estimate, pk=estimate_id)
    context = {'estimate': estimate}
    return render(request, 'estimate/estimate_detail.html', context)

# 견적등록화면
def estimate_create(request):
    if request.method == 'POST':
        form = EstimateForm(request.POST)
        if form.is_valid():
            estimate = form.save(commit=False)
            estimate.reg_date = timezone.now()
            estimate.save()
            return redirect('estimate:index')
    else:
        form = EstimateForm()
    context = {'form': form}
    return render(request, 'estimate/estimate_form.html', context)
