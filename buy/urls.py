from django.urls import path
from . import views

app_name = 'buy'

urlpatterns = [
    path('1/', views.index1, name='index1'),
    path('2/', views.index2, name='index2'),
    path('ing/', views.register_estimate, name='register_estimate'),
    path('estimates/', views.buyer_estimate_list, name='estimate_list'),
    path('estimates/<uuid:estimate_id>', views.buyer_estimate_detail, name='estimate_detail'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('position_choice/', views.position_choice, name='position_choice'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('main/', views.main, name='main'),
    path('', views.main, name='main'),
] 
    
    #path('<uuid:estimate_id>/', views.detail, name='detail'),
    #path('buyer_estimate_list/', views.buyer_estimate_list, name='buyer_estimate_list'),
    
    #path('buyer_estimate_list/<uuid:estimate_id>', views.buyer_estimate_detail, name='buyer_estimate_detail'),

    # ex: /polls/
    # path('', views.IndexView.as_view(), name='index'),
    # # ex: /polls/1/ , name이 detali.html에서 url 템플릿태그 써서 인식할 때 사용됨. url 바꾸려면 템플릿말고 여기서 바꾸면 됌.
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # # ex: /polls/1/results/
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # # ex: /polls/1/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
#]
