from django.shortcuts import render

# Create your views here.
tasks = ["foo", "poo", "goo"]
def index(request):
    return render(request, "mestaches/index.html", {
        "tasks": tasks
    })
    
def add(request):
    return render(request, "mestaches/add.html")    
    