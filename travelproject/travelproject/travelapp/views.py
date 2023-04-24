from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, team


# Create your views here.
def demo(request):
     obj=Place.objects.all()
     obj1=team.objects.all()

     return render(request,'index.html',{'result':obj,'result2':obj1})

