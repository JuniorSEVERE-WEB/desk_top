from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New task")
# Create your views here.

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    return render(request, "tasks/index.html",{
        "tasks":request.session["tasks"]
    })
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            # Récupérer la liste ou la créer si elle n'existe pas
            tasks = request.session.get('tasks', [])
            tasks.append(task)
            # Réassigner la liste pour forcer la sauvegarde de la session
            request.session['tasks'] = tasks
            return HttpResponseRedirect(reverse("index"))
        else:
            # Afficher les erreurs du formulaire
            return render(request, "tasks/add.html", {"form": form})
    # Méthode GET : afficher un formulaire vide
    return render(request, "tasks/add.html", {"form": NewTaskForm()})
