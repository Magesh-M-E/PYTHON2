from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj2=Team.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj2})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     result=x+y
#     return render(request,'result.html',{'res':result})
# #
# def contact(request):
#     return HttpResponse("this is contact")