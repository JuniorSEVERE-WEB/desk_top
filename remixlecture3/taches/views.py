from django.shortcuts import render

tasks = ["foo", "boo", "bii"]
# Create your views here.
def index(request):
    return render(request, "taches/index.html", {
        "tasks": tasks
    })
    
def add(request):
    return render(request, "taches/add.html")    