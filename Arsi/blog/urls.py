
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.show_blog,name='show_blog'),
    path('show/<int:id>', views.detail_blog,name='show_blog'),
]
