import uuid
from django.db import models
from common.models import User
# Create your models here.
# 견적
class Estimate(models.Model):
    estimate_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    buyer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)
    material = models.CharField(max_length=15)
    method = models.CharField(max_length=15)
    pieces = models.IntegerField()
    detail = models.TextField()
    drawing = models.FileField()
    reg_date = models.DateTimeField()
    canBid = models.BooleanField(default=True)

# 입찰
class Bid(models.Model):
    bid_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
    estimate_id = models.ForeignKey(Estimate, on_delete=models.CASCADE)
    price = models.IntegerField()
    bid_date = models.DateTimeField()
    finished = models.BooleanField()

# 거래
class Trade(models.Model):
    trade_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    estimate_id = models.OneToOneField(Estimate, on_delete=models.CASCADE)
    bid_id = models.OneToOneField(Bid, on_delete=models.CASCADE)
    success_date = models.DateTimeField()
    product_state = models.CharField(max_length= 20)
