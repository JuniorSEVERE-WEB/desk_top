from django.shortcuts import redirect, render
from .models import Blog, Comment 
from django.shortcuts import get_object_or_404
from .forms import CommentForm


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
    comments = post.comments.all()
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.posts = post
            comment.save()

            return redirect("detail", pk=pk)
        
    else:
        form = CommentForm()

    return render(request, "detail.html", {
        "post": post,
        "form":form,
        "comments": comments,


    })

def post_like(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.likes += 1
    post.save()
    return redirect("detail", pk=pk)

def search(request):
    query = request.GET.get("q", "")
    results = Blog.objects.filter(title__icontains=query)

    return render(request, "search.html", {
        "query": query, 
        "results": results
        })