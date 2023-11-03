from django.shortcuts import render
from solution.models import Solution
from service.models import Service
from .models import Industry
# Create your views here.


def ShowIndustry(request,id):
    industries = Industry.objects.filter(id=id)
    solutions = Solution.objects.filter(industry_id=id)
    services = Service.objects.filter(industry_id=id)
    context = {'industries':industries,'services':services,'solutions':solutions}
    return render(request,'industry/industry.html',context)
