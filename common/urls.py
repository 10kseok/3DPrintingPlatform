from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('signup_buyer/', auth_views.LoginView.as_view(template_name='common/signup_buyer.html'), name='login'),
    path('signup_seller/', auth_views.LoginView.as_view(template_name='common/signup_seller.html'), name='login'),
]
