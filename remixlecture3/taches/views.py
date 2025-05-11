from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect



class NewTaskForm(forms.Form):
    task = forms.CharField(label="New task")
# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    return render(request, "taches/index.html", {
        "tasks": request.session["tasks"]
    })
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            
            # 1. Vérifier si la clé "task" existe dans la session
            if "task" not in request.session:
                request.session["task"] = []  # Initialiser avec une liste vide
            
            # 2. Ajouter la nouvelle tâche
            request.session["task"] += [task]  # Utiliser += pour étendre la liste
            
            # 3. Sauvegarder explicitement la session (optionnel mais recommandé)
            request.session.modified = True
            
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "taches/add.html", {"form": form})
    
    return render(request, "taches/add.html", {"form": NewTaskForm()})