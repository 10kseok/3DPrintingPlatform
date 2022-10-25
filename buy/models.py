from django.db import models

# Create your models here.
class Buyer(models.Model):
    buyer_id = models.CharField(max_length=30, primary_key=True)
    PW = models.CharField(max_length=30)
    TEL = models.CharField(max_length=20)
    address = models.CharField(max_length=100)