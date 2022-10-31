from django.urls import path
from . import views

app_name = 'buy'
urlpatterns = [
    path('buy/', views.EstimatesView.as_view(), name='buyer_main'),
]
