from email import contentmanager
from multiprocessing import AuthenticationError
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
