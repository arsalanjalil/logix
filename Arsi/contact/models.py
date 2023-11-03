from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models here.


class Comment(models.Model):
    phone = models.CharField(max_length=11, null=False, blank=False, unique=True)
    text = models.TextField(verbose_name='text')
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='user')
    email = models.EmailField(max_length=250, verbose_name='email')
    title = models.CharField(max_length=250, verbose_name='title')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
