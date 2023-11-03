from django.shortcuts import render
from solution.models import Solution

# Create your views here.
def all(request):
    solutions = Solution.objects.all()
    
    context = {'solutions':solutions}
    return render(request,'solution/solution.html',context)

def show(request,id):
        return render(request,'solution/show.html')