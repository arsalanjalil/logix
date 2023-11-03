
from django.contrib import admin
from django.urls import path
from service import views

urlpatterns = [
    path('showsevice/<int:id>', views.show_service,name='show_service'),
    path('show/<int:id>',views.detail_service,name='show'),
    path('product/show/<int:id>',views.detail_product,name='show_product'),
    path('show_order/<int:id>', views.order,name='order'),
]