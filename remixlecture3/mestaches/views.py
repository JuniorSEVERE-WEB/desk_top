from django.shortcuts import render
from django import forms
from django.urls import reverse 
from django.http import HttpResponsePermanentRedirect

# Create your views here.
tasks = ["foo", "poo", "goo"]
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
def index(request):
    return render(request, "mestaches/index.html", {
        "tasks": tasks
    })
    
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponsePermanentRedirect(reverse("index"))
        else:
            return render(request, "mestaches/add.html",{
                "form": NewTaskForm()
            })
    form = NewTaskForm()
    return render(request, "mestaches/add.html",{
        "form": form
    })    
    