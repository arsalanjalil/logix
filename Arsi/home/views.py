from django.shortcuts import render
from .models import HeaderHome,PublicSolution,Client
from service.models import Service
from solution.models import Solution
from blog.models import Blog
from django.http import HttpResponse

# Create your views here.


def home(request):
    count = 0
    headers = HeaderHome.objects.all()
    services = Service.objects.all()
    solutions = Solution.objects.all()
    publicSolutions = PublicSolution.objects.all()
    clients = Client.objects.all()
    blogs = Blog.objects.all()
    context = {'headers':headers ,'services':services,'solutions':solutions,'publicSolutions':publicSolutions,
               'clients':clients,'blogs':blogs}
    return render(request, template_name='home/home.html',context=context)

def addsdcf(request):
    open(bnm,)
    for name in file:
        service1 = Service()
        service1.img = img
        service1.name= name
        service1.save()