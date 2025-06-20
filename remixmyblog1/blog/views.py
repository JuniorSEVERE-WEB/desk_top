from django.shortcuts import render

# Create your views here.
def blog_list(request):
    return render(request, "blog/list.html")

def posts_detail(request, id):
    return render(request, "blog/detail.html")