from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('', views.BoardListView.as_view(), name='home'),
    path('boards/<str:board_name>/', views.board_topics, name='board_topics'),
    path('boards/<str:board_name>/new/', views.new_topic, name='new_topic'),
    path('boards/<str:board_name>/topics/<int:topic_id>/', views.topic_posts, name='topic_posts'),
    path('boards/<str:board_name>/topics/<int:topic_id>/reply/', views.reply_topic, name='reply_topic'),
    path('boards/<str:board_name>/topics/<int:topic_id>/posts/<int:post_id>/edit', views.EditPostView.as_view(), name='edit_post'),
]
