from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    flag = models.CharField(max_length=20)
    last_name = None 
    TEL = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    equipment_id1 = models.CharField(max_length=50, blank=True)
    equipment_id2 = models.CharField(max_length=50, blank=True)
    equipment_id3 = models.CharField(max_length=50, blank=True)
    equipment_id4 = models.CharField(max_length=50, blank=True)
    equipment_id5 = models.CharField(max_length=50, blank=True)