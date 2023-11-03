from django.urls import path
from about import views
urlpatterns = [
    path('', views.about,name='show_about'),
    path('privacy-policy', views.policy,name='policy'),
]