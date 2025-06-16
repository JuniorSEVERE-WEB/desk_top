from django.shortcuts import render
from .models import Blog, Comment 
# Create your views here.
def blog_list(request):
    posts = Blog.objects.all()
    carousel = Blog.objects.all().order_by("-id")[:4]
    return render(request, "list.html", {
        "posts": posts,
        "carousel": carousel
    })

def blog_detail(request):
    return render(request, "detail.html")