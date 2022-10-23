from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('', views.home, name='home'),
    path('boards/<str:board_name>/', views.board_topics, name='board_topics'),
    path('boards/<str:board_name>/new/', views.new_topic, name='new_topic'),
    path('boards/<str:board_name>/topics/<int:topic_id>/', views.topic_posts, name='topic_posts')
]
