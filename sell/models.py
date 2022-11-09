from django.db import models

# Create your models here.
class Equipment(models.Model):
    method = models.CharField(max_length=50)
    material = models.CharField(max_length=100)

# class EquipmentToSeller(models.Model):
#     seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
#     equipment_id = models.ForeignKey(Equipment, on_delete=models.CASCADE)

