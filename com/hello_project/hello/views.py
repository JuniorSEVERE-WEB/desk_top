from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def junior(request):
    return HttpResponse("Bonjour Junior!")

def severe(request):
    return HttpResponse("Bonjour SEVERE!")

def pierre(request):
    return HttpResponse("Bonjour Pierre!")


