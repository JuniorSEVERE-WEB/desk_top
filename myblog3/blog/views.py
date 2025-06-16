from django.shortcuts import render
from .models import Blog, Comment 
from django.shortcuts import get_object_or_404

# Create your views here.
def blog_list(request):
    posts = Blog.objects.all()
    carousel = Blog.objects.all().order_by("-id")[:4]
    return render(request, "list.html", {
        "posts": posts,
        "carousel": carousel
    })

def blog_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    return render(request, "detail.html", {
        "post": post

    })