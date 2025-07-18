from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render 
# Create your views here.

def index(request):
    return render(request, "singlepage/index.html")

def bonjour(request):
    name = request.GET.get("name", "")
    return JsonResponse({"message": f"Bonjour {name}!"})
