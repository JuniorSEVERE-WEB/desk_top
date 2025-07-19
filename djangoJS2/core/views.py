from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request, "core/index.html")

def get_message(request):
    data = {
        "message": "Junior travaille son premier projet django-javascript"
    }
    return JsonResponse(data)
