from django.db import models
from api_store.settings import STATIC_URL as static
from ckeditor.fields import RichTextField
# Create your models here.


class HeaderHome(models.Model):
    name = models.CharField(max_length=200, verbose_name='name')
    title = models.CharField(max_length=250,verbose_name='title')
    description = RichTextField()
    img = models.ImageField(upload_to='public/images/home/headers',verbose_name='img')
    alt = models.CharField(max_length=200, verbose_name='alt')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#    class Meta:
#       app_label  = 'HeaderHome'

    def url(self, short=False):
        if short is False:
            return static + self.img.url[7:]
        return self.img.url[7:]



class PublicSolution(models.Model):
    title = models.CharField(max_length=250,verbose_name='title')
    description = models.TextField(verbose_name='description')
    img = models.ImageField(upload_to='public/images/home/publicSolution', verbose_name='img')
    alt = models.CharField(max_length=200, verbose_name='alt')

#    class Meta:
#        app_label  = 'PublicSolution'

    def url(self, short=False):
        if short is False:
            return static + self.img.url[7:]
        return self.img.url[7:]

    def url(self, short=False):
        if short is False:
            return static + self.img.url[7:]
        return self.img.url[7:]


class Client(models.Model):
    name = models.CharField(max_length=200, verbose_name='name')
    field = models.CharField(max_length=250,verbose_name='field')
    comment = models.TextField(verbose_name='comment')
    like = models.IntegerField(default=0, verbose_name='score')
    img = models.ImageField(upload_to='public/images/home/client',verbose_name='img')
    alt = models.CharField(max_length=200, verbose_name='alt')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


#    class Meta:
#        app_label  = 'Client'

    def url(self, short=False):
        if short is False:
            return static + self.img.url[7:]
        return self.img.url[7:]

class Social(models.Model):
    link = models.CharField(max_length=250,verbose_name='link')
    img = models.ImageField(upload_to='public/images/home/social',verbose_name='image')


#    class Meta:
#        app_label  = 'Social'

    def url(self, short=False):
        if short is False:
            return static + self.img.url[7:]
        return self.img.url[7:]
