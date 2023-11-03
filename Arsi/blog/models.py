from django.db import models
from api_store.settings import STATIC_URL as static
from ckeditor.fields import RichTextField
from datetime import datetime
# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=250, verbose_name='name', null=True)
    title = models.CharField(max_length=250, verbose_name='title', null=True)
    description = RichTextField()
    short_description = models.TextField(null=True, verbose_name='short_description')
    img = models.ImageField(upload_to='public/images/blogs/blog', verbose_name='img', null=True)
    alt = models.CharField(max_length=200, verbose_name='alt')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def url(self, short=False):
        if short is False:
            return static + self.img.url[7:]
        return self.img.url[7:]

    def show_date(self):

        return self.created_at.strftime("%A %B %d, %Y")
