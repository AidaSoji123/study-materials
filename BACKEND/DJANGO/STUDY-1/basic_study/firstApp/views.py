from django.http import  HttpResponse
from django.shortcuts import render

# Create your views here.
def greeting(request):
    return HttpResponse("Hellooooo Mayaavii...")