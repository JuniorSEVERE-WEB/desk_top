from django.shortcuts import render
from django import forms
from django.urls import reverse 
from django.http import HttpResponsePermanentRedirect

# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
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
            request.session["tasks"]+= [task]
            return HttpResponsePermanentRedirect(reverse("index"))
        else:
            return render(request, "mestaches/add.html",{
                "form": NewTaskForm()
            })
    form = NewTaskForm()
    return render(request, "mestaches/add.html",{
        "form": form
    })    
    