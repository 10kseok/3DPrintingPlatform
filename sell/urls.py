from django.urls import path
from . import views

app_name = 'sell'
urlpatterns = [
    path('seller/', views.EstimatesView.as_view(), name='seller_kanban'),
    # ex: /polls/
    # path('', views.IndexView.as_view(), name='index'),
    # # ex: /polls/1/ , name이 detali.html에서 url 템플릿태그 써서 인식할 때 사용됨. url 바꾸려면 템플릿말고 여기서 바꾸면 됌.
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # # ex: /polls/1/results/
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # # ex: /polls/1/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
