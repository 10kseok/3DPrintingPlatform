from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import SignupForm, EquipmentForm
from sell.models import Equipment
# Create your views here.

def index(request):
    return render(request, '../templates/common/temp/05_메인(로그인전).html')

def mypage(request):
    if request.user.flag == "SELLER":
        user = request.user
        equipment = Equipment.objects.get(pk=user.equipment_id1) 
        method = equipment.method
        materials = equipment.material.split('/')
    return render(request, 'common/temp/마이페이지.html', {
                                                        'method': method,
                                                        'materials': materials
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