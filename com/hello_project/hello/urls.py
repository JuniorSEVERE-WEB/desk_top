from django.urls import path 
from . import views 

urlpatterns = [
    path("junior/", views.junior),
    path("severe/", views.severe),
    path("pierre/", views.pierre),
]
