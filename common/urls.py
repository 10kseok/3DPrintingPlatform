from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='../templates/common/temp/07_로그인.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/buyer', views.signup_buyer, name='signup_buyer'),
    path('signup/seller', views.signup_seller, name='signup_seller'),
    path('signup/', views.signup, name='signup'),
    path('mypage/', views.mypage, name='mypage')
]
