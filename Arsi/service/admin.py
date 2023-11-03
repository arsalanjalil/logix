from django.contrib import admin
from service.models import Order,Product,Feature,Detaile,Property,Service
# Register your models here.

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Feature)
admin.site.register(Detaile)
admin.site.register(Property)

