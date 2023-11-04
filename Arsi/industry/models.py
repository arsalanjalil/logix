from django.db import models
from api_store.settings import STATIC_URL as static
from ckeditor.fields import RichTextField
# Create your models here.


class Industry(models.Model):
    name = models.CharField(max_length=250, verbose_name='name', null=True)
    title = models.CharField(max_length=250, verbose_name='title', null=True)
    description = RichTextField()
    short_description = RichTextField()
    banner = models.ImageField(upload_to='public/images/industries/industries', verbose_name='banner', null=True)
    alt = models.CharField(max_length=200, verbose_name='alt')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label  = 'industry'

    def url(self, short=False):
        if short is False:
            return static + self.banner.url[7:]
        return self.banner.url[7:]
