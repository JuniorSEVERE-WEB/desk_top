from django.shortcuts import render
from django import forms 
from django.http import HttpResponseRedirect
from django.urls import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    
# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "mestaches1/index.html", {
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
            return render(request, "mestaches1/add.html", {
                "form": form
            })
        
    return render(request, "mestaches1/add.html", {
        "form": NewTaskForm()
    })    

def delete(request, task_id):
    tasks = request.session.get("tasks", [])
    if task_id < 0 or task_id >= len(tasks):
        return HttpResponseRedirect(reverse("index"))
    
    if request.method == "POST":
        del tasks[task_id]
        request.session["tasks"] = tasks
        return HttpResponseRedirect(reverse("index"))
    
    return render(request, "mestaches1/delete.html",{
        "task": tasks[task_id],
        "task_id": task_id
    })
        
    
    