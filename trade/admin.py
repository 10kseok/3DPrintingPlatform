from django.contrib import admin
from .models import *

# Register your models here.
# 관리자 계정에서 모델들을 다룰 수 있게
for model in [Estimate, Bid, Trade]:
    admin.site.register(model)