from django.urls import path 
from . import views 

urlpatterns = [
    path("",views.blog_list, name="list"),
    path("posts/<int:id>/", views.posts_detail, name="detail")
    
]
