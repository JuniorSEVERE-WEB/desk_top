from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.blog_list, name="list"),
    path("posts/<int:pk>/", views.blog_detail, name="detail")
]
