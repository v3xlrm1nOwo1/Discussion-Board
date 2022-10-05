from enum import unique
from msvcrt import open_osfhandle
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Board Table
class Board(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Topic Table
class Topic(models.Model):
    subject = models.CharField(max_length=700)
    board = models.ForeignKey(Board, related_name="topics", on_delete=models.CASCADE)
    create_by = models.ForeignKey(User, related_name="topics", on_delete=models.CASCADE)
    create_dt = models.DateTimeField(auto_now_add=True)


# Post Table
class Post(models.Model):
    subject = models.TextField(max_length=5000)
    board = models.ForeignKey(Topic, related_name="posts", on_delete=models.CASCADE)
    create_by = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    create_dt = models.DateTimeField(auto_now_add=True)