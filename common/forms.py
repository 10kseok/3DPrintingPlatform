from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from sell.models import Equipment

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'password', 'TEL', 'address']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'TEL': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        labels = {
            'username': '아이디',
            'first_name': '이름',
            'password': '비밀번호',
            'TEL': '전화번호', 
            'address': '주소',
        }  

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = "__all__"
