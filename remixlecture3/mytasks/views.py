from django.shortcuts import render
from django import forms 
from django.http import HttpResponseRedirect
from django.urls import reverse 


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
   
# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    return render(request, "mytasks/index.html", {
        "tasks": request.session["tasks"]
    })
    
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "mytasks/add.html",{
                "form":form 
            })        
    return render(request, "mytasks/add.html",{
        "form": NewTaskForm()
    })