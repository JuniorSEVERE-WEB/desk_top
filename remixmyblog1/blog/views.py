from django.shortcuts import render
from .models import Blog, Comment

# Create your views here.
def blog_list(request):
    posts = Blog.objects.all()
    
    return render(request, "blog/list.html",{
        "posts":posts,
        
    })

def posts_detail(request, id):
    return render(request, "blog/detail.html")