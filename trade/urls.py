from django.urls import path

from . import views
app_name = 'trade'

urlpatterns = [
    path('buy/complete/<uuid:bid_id>', views.buy_complete, name='buy_complete'),
    path('sell/complete/', views.sell_complete, name='sell_complete'),
]