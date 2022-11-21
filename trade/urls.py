from django.urls import path

from . import views
app_name = 'trade'

urlpatterns = [
    path('buy/complete/<uuid:bid_id>', views.buy_complete, name='buy_complete'),
    path('sell/complete/<uuid:bid_id>', views.sell_complete, name='sell_complete'),
]