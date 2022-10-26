from django.db import models

# Create your models here.
"""class Buyer(models.Model):
    buyer_id = models.CharField(max_length=30, primary_key=True)
    PW = models.CharField(max_length=30)
    TEL = models.CharField(max_length=20)
    address = models.CharField(max_length=100)"""

class Estimate(models.Model):
    project_name = models.CharField(max_length=30)
    material = models.CharField(max_length=15)
    method = models.CharField(max_length=15)
    pieces = models.IntegerField()
    detail = models.TextField()
    drawing = models.FileField()
    reg_date = models.DateTimeField()
    def __str__(self):
        return self.project_name  # 임시로
