from django.shortcuts import render
from solution.models import Solution,Image

# Create your views here.
def all(request):
    solutions = Solution.objects.all()
    #images= Images.objects.all()
    context = {'solutions':solutions}
    return render(request,'solution/solution.html',context)

def show(request,id):
        solutions = Solution.objects.filter(id=id)
        context = {'solutions': solutions}
        return render(request,'solution/show.html',context)