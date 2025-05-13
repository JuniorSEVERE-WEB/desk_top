from django.shortcuts import render
from django import forms 
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New task")
    
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    return render(request, "mestaches/index.html", {
        "tasks": request.session["tasks"]
    })
    
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            
            tasks = request.session.get("tasks", [])
            tasks.append(task)
            
            request.session["tasks"] = tasks 
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "mestaches/add.html", {
                "form": form 
            })
    return render(request, "mestaches/add.html",{
        "form": NewTaskForm()
    })   
