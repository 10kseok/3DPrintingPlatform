from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.
class BuyerForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    TEL = forms.CharField(max_length=20, label="전화번호")
    address = forms.CharField(max_length=100, label="주소")

    model = User
    fields = ("buyer_id", "PW1", "PW2", "email", "TEL", "address")

class SellerForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    TEL = forms.CharField(max_length=20, label="전화번호")
    address = forms.CharField(max_length=100, label="주소")
    equipment_id1 = forms.CharField(max_length=50, label="장비ID")

    model = User
    fields = ("seller_id", "PW1", "PW2", "email", "TEL", "address", "equipment_id1")
