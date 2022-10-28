from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
# Create your models here.


# Board Table
class Board(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    # return posts count
    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()
    
    # return last post
    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by("-created_dt").first()


# Topic Table
class Topic(models.Model):
    subject = models.CharField(max_length=700)
    board = models.ForeignKey(Board, related_name="topics", on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name="topics", on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.subject


# Post Table
class Post(models.Model):
    comment = models.TextField(max_length=5000)
    topic = models.ForeignKey(Topic, related_name="posts", on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE, null=True)
    update_by = models.DateTimeField(null=True)
    
    def __str__(self):
        
        com = Truncator(self.comment)
        return com.chars(30)