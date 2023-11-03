from django.db import models
from api_store.settings import STATIC_URL as static
from ckeditor.fields import RichTextField
from django.contrib import admin
from industry.models import Industry
# Create your models here.


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
    title = models.CharField(max_length=250, verbose_name='title',null=True)
    description = RichTextField()
    short_description = models.TextField(null=True, verbose_name='short_description')
    service = models.ForeignKey(Service , on_delete=models.CASCADE,verbose_name='service_id')
    img = models.ImageField(upload_to='public/images/services/service',verbose_name='img',null=True)
    alt = models.CharField(max_length=200, verbose_name='alt')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def url(self, short=False):
        if short is False:
            return static + self.img.url[7:]
        return self.img.url[7:]
    
class Property(models.Model):
    name = models.CharField(max_length=250, verbose_name='name',null=True)
    title = models.TextField() 
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    svg = models.TextField()

class Feature(models.Model):
    name = models.CharField(max_length=250, verbose_name='name',null=True)
    title = models.TextField() 
    img = models.ImageField(upload_to='public/images/services/service',verbose_name='img',null=True)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)

class Detaile(models.Model):
    detail = models.CharField(max_length=250, verbose_name='name',null=True)   
    svg = models.TextField()
    feature = models.ForeignKey(Feature , on_delete=models.CASCADE)
