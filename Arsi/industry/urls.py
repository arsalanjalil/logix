
from django.contrib import admin
from django.urls import path
from industry import views

urlpatterns = [
    path('show/<int:id>',views.ShowIndustry,name='show_industry'),
]