from bs4 import FeatureNotFound
from django.db import models
from industry.models import Industry
from api_store.settings import STATIC_URL as static
from ckeditor.fields import RichTextField


class Solution(models.Model):
    name =  models.CharField(max_length=250, verbose_name="name")
    title = models.CharField(max_length=250, verbose_name='title', null=True)
    description = RichTextField()
    long_description = RichTextField(verbose_name='Long Description',null=True,default='')
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, null=True,blank=True)
    img = models.ImageField(upload_to='public/images/solution/solutions', verbose_name='banner', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def url(self, short=False):
        if short is False:
            return static + self.img.url[7:]
        return self.img.url[7:]

    def __str__(self):
        return self.name
    
    def short_title(self):
        words = self.title.split()

    # Check if the number of words is greater than 10
        if len(words) > 7:
            # Return the first 10 words
            return ' '.join(words[:7])+'...'
        else:
        # If the number of words is 10 or fewer, return the original string
            return self.title

        
class Feature(models.Model):
    feature = models.CharField(max_length=250, verbose_name="name")
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE, null=True,blank=True)
    img = models.ImageField(upload_to='public/images/solution/solutions/features', verbose_name='banner', null=True)
    code = models.TextField(default=" ")

    def url(self, short=False):
        if short is False:
            return static + self.img.url[7:]
        return self.img.url[7:]

    def __str__(self):
        return self.feature
    

class Image(models.Model):
    img = models.ImageField(upload_to='public/images/industries/industries', verbose_name='banner', null=True)
    alt = models.CharField(max_length=200, verbose_name='alt')
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE, null=True,blank=True)
    
    def url(self, short=False):
        if short is False:
            return static + self.img.url[7:]
        return self.img.url[7:]


class Question(models.Model):
        solution = models.ForeignKey(Solution, on_delete=models.CASCADE, null=True,blank=True)
        question = RichTextField()    
        answer = RichTextField()
