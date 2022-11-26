from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import SignupForm
from sell.models import Equipment
from trade.models import Trade, Bid, Estimate
# Create your views here.

def index(request):
    return render(request, '../templates/common/temp/05_메인(로그인전).html')

def mypage(request):
    user = request.user

    # TODO: 거래내역 불러오기 ( input = 유저ID, output = Trade )
    if user.flag == "SELLER":
        equipment = Equipment.objects.get(pk=user.equipment_id1) 
        method = equipment.method
        materials = equipment.material.split('/')
        # ** 생산자는 Estimate에 포함된 속성이 아니기에 Bid를 먼저 조회한다. **
        # 자신이 입찰한 Bid 중 낙찰된 Bid 불러오기
        bid_log = Bid.objects.filter(seller_id=user, finished=True)
        # 낙찰된 Bid_id로 Trade 불러오기
        trade_log = Trade.objects.filter(bid_id__in=bid_log).order_by('-success_date')
        
    elif user.flag == "BUYER":
        method, materials = '', ''
        # ** 구매자는 Estimate에 포함된 속성이므로 Estimate부터 조회한다. **
        # 자신이 등록한 Estimate 데이터를 불러온다.
        estimate_log = Estimate.objects.filter(buyer_id=user)
        # Bid를 통해 Trade 불러오기
        trade_log = Trade.objects.filter(estimate_id__in=estimate_log).order_by('-success_date')

 
    return render(request, 'common/temp/마이페이지.html', {
                                                        'method': method,
                                                        'materials': materials,
                                                        'trade_log': trade_log,
                                                        })

def signup(request):
    return render(request, '../templates/common/temp/12_회원가입(포지션선택).html')

def signup_buyer(request):
    if request.method == "POST":
        default_form = SignupForm(request.POST)

        if default_form.is_valid():
            # commit=False => 저장하지 않고 객체 반환
            user = default_form.save(commit=False)
            user.flag = "BUYER"
            user.save()

            username = default_form.cleaned_data.get('username')
            raw_password = default_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        default_form = SignupForm()
    return render(request, '../templates/common/temp/13_회원가입(의뢰인).html', {'form': default_form})

def signup_seller(request):
    if request.method == "POST":
        method = request.POST.get('method')
        materials = request.POST.getlist('materials[]')
        materials_for_DB = "/".join(materials)
        default_form = SignupForm(request.POST)

        if default_form.is_valid():
            equipment = Equipment(method=method, material=materials_for_DB)
            equipment.save()
            user = default_form.save(commit=False)
            user.equipment_id1 = equipment.pk
            user.flag = "SELLER"
            user.save()

            username = default_form.cleaned_data.get('username')
            raw_password = default_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')

    else:
        default_form = SignupForm()

    return render(request, '../templates/common/temp/14_회원가입(생산자).html', {'form': default_form})

