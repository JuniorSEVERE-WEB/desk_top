from django.shortcuts import render
from django.http import HttpResponse
from .forms import contactForm
# Create your views here.

def contact(request):
    
    form = contactForm()
    return render(request, 'myapp/form.html', {
        'form': form 
    })
