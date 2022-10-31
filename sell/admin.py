from django.contrib import admin
from .models import *

# Register your models here.
for model in [Equipment, Seller, EquipmentToSeller]:
    admin.site.register(model)