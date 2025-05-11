from django.shortcuts import render


tasks = ["foo", "bar", "gaz"]
# Create your views here.
def index(request):
    return render(request, "mytasks/index.html", {
        "tasks": tasks
    })
    
def add(request):
    return render(request, "mytasks/add.html")