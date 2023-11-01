
from django.contrib import admin
from django.urls import path
from solution import views

urlpatterns = [
    path('all', views.all,name='all_solution'),
    path('show/<int:id>',views.show,name='show_solution'),

]