from django.urls import path
from . import views

app_name = 'sell'
urlpatterns = [
    path('bid_board/', views.bid_board, name='bid_board'),
    path('bid_board/<uuid:estimate_id>', views.estimate_detail, name='estimate_detail'),
]
