from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('', views.home, name='home'),
    path('boards/<str:board_name>/', views.board_topics, name='board_topics'),
]
