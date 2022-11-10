from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import SignupForm, EquipmentForm
# Create your views here.

def index(request):
    return render(request, '../templates/common/temp/05_메인(로그인전).html')

def signup(request):
    return render(request, '../templates/common/temp/12_회원가입(포지션선택).html')

def signup_buyer(request):
    if request.method == "POST":
        print("request.POST", request.POST)
        form = SignupForm(request.POST)
        # print("form", form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, '../templates/common/temp/13_회원가입(의뢰인).html', {'form': form})

def signup_seller(request):
    if request.method == "POST":
        print(request.POST)
        # form = SignupForm(request.POST)
        # print("form", form)
        # if form.is_valid():
        #     form.save()
        #     username = form.cleaned_data.get('username')
        #     raw_password = form.cleaned_data.get('password1')
        #     user = authenticate(username=username, password=raw_password)  # 사용자 인증
        #     login(request, user)  # 로그인
        #     return redirect('index')
    else:
        default_form = SignupForm()
        extra_form = EquipmentForm()

    return render(request, '../templates/common/temp/14_회원가입(생산자).html',
                    {'default_form': default_form, 'extra_form': extra_form})