from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.blog_list, name="list"),
    path("posts/", views.post_detail, name="detail")
]
