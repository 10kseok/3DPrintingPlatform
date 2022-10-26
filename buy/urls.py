from django.urls import path

from . import views

app_name = 'buy'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:estimate_id>/', views.detail, name='detail'),
    path('estimate/create/', views.estimate_create, name='estimate_create'),
]
