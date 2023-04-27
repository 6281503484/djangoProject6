from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class Input(View):
    def get(self,request):
        return render(request,'getinput.html')
class Add(View):
    def get(self,request):
        x=request.GET["t1"]
        y=request.GET["t2"]
        i=int(x)
        j=int(y)
        k=i+j
        res=HttpResponse("the result is:" +str(k))
        return res





