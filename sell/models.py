from django.db import models

# Create your models here.
class Equipment(models.Model):
    equipment_id = models.CharField(max_length=50, primary_key=True)
    method = models.CharField(max_length=50)
    material = models.CharField(max_length=100)

class Seller(models.Model):
    seller_id = models.CharField(max_length=30, primary_key=True)
    PW = models.CharField(max_length=30)
    TEL = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    equipment_id1 = models.CharField(max_length=50)
    equipment_id2 = models.CharField(max_length=50)
    equipment_id3 = models.CharField(max_length=50)
    equipment_id4 = models.CharField(max_length=50)
    equipment_id5 = models.CharField(max_length=50)
    equipment_id6 = models.CharField(max_length=50)
    equipment_id7 = models.CharField(max_length=50)
    equipment_id8 = models.CharField(max_length=50)
    equipment_id9 = models.CharField(max_length=50)
    equipment_id10 = models.CharField(max_length=50)

class EquipmentToSeller(models.Model):
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    equipment_id = models.ForeignKey(Equipment, on_delete=models.CASCADE)

