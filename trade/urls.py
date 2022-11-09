from django.urls import path

from . import views

urlpatterns = [
    path('buy/complete/', views.buy_complete, name='buy_complete'),
    path('sell/complete/', views.sell_complete, name='sell_complete'),
]