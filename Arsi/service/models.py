from django.db import models
from api_store.settings import STATIC_URL as static
from ckeditor.fields import RichTextField
from django.contrib import admin
from industry.models import Industry
# Create your models here.
from faicon.fields import FAIconField


import random


class Service(models.Model):
    name = models.CharField(max_length=250, verbose_name='name',null=True)
    title = models.CharField(max_length=250, verbose_name='title',null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, db_constraint=False, default=0,)
    industry = models.ForeignKey(Industry,on_delete=models.CASCADE, null=True,blank=True)
    description = RichTextField()
    short_description = models.TextField(null=True, verbose_name='short_description')
    img = models.ImageField(upload_to='public/images/services/service',verbose_name='img',null=True)
    icon = models.CharField(max_length=200, null=True, verbose_name='icon')
    alt = models.CharField(max_length=200, verbose_name='alt')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    def url(self, short=False):
        if short is False:
            return static + self.img.url[7:]
        return self.img.url[7:]
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'title']
    search_fields = ('name',)
    autocomplete_fields = ['parent']



    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['title'].required = False
        form.base_fields['name'].required = False
        form.base_fields['img'].required = False
        form.base_fields['parent'].required = False
        form.base_fields['icon'].required = False
        form.base_fields['alt'].required = False
        form.base_fields['industry'].required = False


        return form


class Order(models.Model):
    STATE = [(0, 'Important'), (1, ' No matter'), (2, 'It does not matter much'),]
    state = models.PositiveSmallIntegerField(choices=STATE, default=0, verbose_name='state')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='service_id')
    file = models.FileField(upload_to='public/files/file',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




    def __str__(self):
        return self.service.name

    def default_state(self):
        return self.state


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='name',null=True)
    title = models.CharField(max_length=250, verbose_name='title',null=True,blank=True)
    description = RichTextField()
    short_description = models.TextField(null=True, verbose_name='short_description')
    service = models.ForeignKey(Service , on_delete=models.CASCADE,verbose_name='service_id')
    img = models.ImageField(upload_to='public/images/services/service',verbose_name='img',null=True)
    alt = models.CharField(max_length=200, verbose_name='alt')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    def url(self, short=False):
        if short is False:
            return static + self.img.url[7:]
        return self.img.url[7:]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'title',]
    search_fields = ('name',)

class Property(models.Model):
    name = models.CharField(max_length=250, verbose_name='name',null=True)
    title = models.TextField() 
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    svg = models.TextField()

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=250, verbose_name='name',null=True)
    title = models.TextField() 
    img = models.ImageField(upload_to='public/images/services/service',verbose_name='img',null=True)
    service = models.ForeignKey(Service , on_delete=models.CASCADE,default=0)

    def __str__(self):
        return self.name

    def url(self, short=False):
        if short is False:
            return static + self.img.url[7:]
        return self.img.url[7:]

class Detaile(models.Model):
    detail = models.CharField(max_length=250, verbose_name='name',null=True)   
    icon = FAIconField()
    feature = models.ForeignKey(Feature , on_delete=models.CASCADE)

    def __str__(self):
        return self.detail

    def showIcon(self):
        return self.icon.icon_html() 
 

class OurFeature(models.Model):
    name = models.CharField(max_length=250, verbose_name='name',null=True)
    icon = FAIconField()
    service = models.ForeignKey(Service , on_delete=models.CASCADE,default=0)

    def __str__(self):
        return self.name

    colors = ['#ADFF2F','#7FFF00','#7CFC00','#00FF00','#32CD32','#98FB98',
    '#90EE90',
    '#00FA9A',
    '#00FF7F',
    '#3CB371',
    '#2E8B57',
    '#228B22',
    '#008000',
    '#006400',
    '#9ACD32',
    '#6B8E23',
    '#556B2F',
    '#66CDAA',
    '#8FBC8F',
    '#20B2AA',
    '#008B8B',
    '#008080']

    def color(self):
        return random.choice(self.colors)


