from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("junior/", views.junior, name="junior"),
    path("<str:name>", views.greet, name="greet"),
]