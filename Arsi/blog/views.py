from django.shortcuts import render
from .models import Blog
# Create your views here.


def show_blog(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request,'blog/blog.html',context)


def detail_blog(request,id):
    blogs = Blog.objects.filter(id=id)
    context = {'blogs': blogs, }
    return render(request, 'blog/detail_blog.html', context)