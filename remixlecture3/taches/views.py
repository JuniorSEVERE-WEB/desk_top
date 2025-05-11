from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
tasks = ["foo", "boo", "bii"]
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New task")
# Create your views here.
def index(request):
    return render(request, "taches/index.html", {
        "tasks": tasks
    })
    
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "taches/add.html",
                          {
                              "form": form
                          })
    return render(request, "taches/add.html",{
        "form": NewTaskForm()
    })    