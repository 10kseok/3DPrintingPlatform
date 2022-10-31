from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import BuyerForm, SellerForm

# Create your views here.
def index(request):
    page = request.GET.get('page')
    context = {'main_before_login': page}
    return render(request, 'main_before_login.html', context)


def signup_buyer(request):
    if request.method == "POST":
        form = BuyerForm(request.POST)
        if form.is_valid():
            form.save()
            buyer_id = form.cleaned_data.get('buyer_id')
            raw_password = form.cleaned_data.get('PW1')
            buyer = authenticate(buyer_id=buyer_id, PW1=raw_password)  # 사용자 인증
            login(request, buyer)  # 로그인
            return redirect('index')
    else:
        form = BuyerForm()
    return render(request, 'common/signup_buyer.html', {'form': form})

def signup_seller(request):
    if request.method == "POST":
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            seller_id = form.cleaned_data.get('seller_id')
            raw_password = form.cleaned_data.get('PW1')
            seller = authenticate(seller_id=seller_id, PW1=raw_password)  # 사용자 인증
            login(request, seller)  # 로그인
            return redirect('index')
    else:
        form = SellerForm()
    return render(request, 'common/signup_seller.html', {'form': form})
