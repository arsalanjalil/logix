
from django.contrib import admin
from django.urls import path
from service import views

urlpatterns = [
    path('', views.service,name='show_service'),
    path('show/<int:id>',views.detail_service,name='show'),
]