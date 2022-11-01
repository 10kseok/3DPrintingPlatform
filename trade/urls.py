from django.urls import path

from . import views

urlpatterns = [
    path('', views.estimate),
    path('', views.bid),
    path('', views.trade),
]