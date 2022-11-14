from django.urls import path
from . import views

app_name = 'buy'

urlpatterns = [
    path('register/', views.register_estimate, name='register_estimate'),
    path('estimates/', views.estimate_list, name='estimate_list'),
    path('estimates/<uuid:estimate_id>', views.estimate_detail, name='estimate_detail'),
    path('', views.main, name='main'),
] 
