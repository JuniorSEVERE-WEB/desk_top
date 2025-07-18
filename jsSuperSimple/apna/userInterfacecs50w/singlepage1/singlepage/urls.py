from django.urls import path  

from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("bonjour", views.bonjour, name="bonjour")
]
