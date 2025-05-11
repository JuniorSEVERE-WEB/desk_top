from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.contact, name="index"),
    path("snippet", views.snippet_detail, name="snippet_detail")
]