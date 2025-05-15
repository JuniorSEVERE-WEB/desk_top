from django.shortcuts import render
from django import forms 
from django.urls import reverse 
from django.http import HttpResponseRedirect



class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    
# Create your views here.
def index(request):
    tasks = request.session.get("tasks", ["boo", "foo"])
    return render(request, "tasks/index.html", {
        "tasks":tasks 
    })
    
def add(request):
    tasks = request.session.get("tasks", [])
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            
            request.session["tasks"] = tasks 
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form 
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })        
    
def delete(request, task_id):
    tasks = request.session.get("tasks", [])
     
    
    if task_id < 0 or task_id >= len(tasks):
        return HttpResponseRedirect(reverse("index"))
    
    if request.method == "POST":
        del tasks[task_id]
        request.session["tasks"]=tasks
        
        return HttpResponseRedirect(reverse("index"))
    
    return render(request, "tasks/delete.html", {
        "task": tasks[task_id],
        "task_id": task_id
    })
            
def update(request, task_id):
    tasks = request.session.get("tasks", [])
    
    if task_id < 0 or task_id >= len(tasks):
        return HttpResponseRedirect(reverse("index"))
    
                
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        
        if form.is_valid():
            tasks[task_id] = form.cleaned_data["task"]
            request.session["tasks"] = tasks 
            return HttpResponseRedirect(reverse("index"))
        
    form = NewTaskForm(initial = {"task":tasks[task_id]})
    
    return render(request, "tasks/update.html", {
        "form": form,
        "task_id": task_id
    })    
                    
            