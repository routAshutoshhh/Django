from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello, world!")
    return render(request,'website/index.html') # when we get request , we need to return the index file 

def about(request):
    return HttpResponse("Hello, world! I am about")

def contact(request):
    return HttpResponse("Hello, world! I am contact") 