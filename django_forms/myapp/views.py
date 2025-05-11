from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import contactForm, SnippetForm
# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(name, email)
            
    else:
        form = contactForm()  # Formulaire vide pour les GET
    
    # Ce return est EXÉCUTÉ DANS TOUS LES CAS sauf après un formulaire valide
    return render(request, 'myapp/form.html', {'form': form})


def snippet_detail(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            print("Valid!")
   
    form = SnippetForm()  # Formulaire vide pour les GET
    
    # Ce return est EXÉCUTÉ DANS TOUS LES CAS sauf après un formulaire valide
    return render(request, 'myapp/form.html', {'form': form})

    