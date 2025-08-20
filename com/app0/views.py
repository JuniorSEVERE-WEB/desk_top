from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, "app0/login.html")

def logout_view(request):
    return render(request, "app0/login.html")

def index(request):
    return render(request, "app0/index.html")

def register(request):
    return render(request, "app0/register.html")
