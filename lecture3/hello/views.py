from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello world!</h1>")

def junior(request):
    return HttpResponse("<h1>Hello Junior!</h1>")

def greet(request, name):
    return HttpResponse(f"Hello {name.capitalize()}")