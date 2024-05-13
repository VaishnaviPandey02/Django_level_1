from django.shortcuts import render
from django.http import HttpResponse
#request->response
#request handler    
# Create your views here.

def calculate(request):
    x=1
    y=2
    return x
def say_hello(request):
   x=calculate()
   return render(request,'hello.html',{'name':'Vaishnavi'})
