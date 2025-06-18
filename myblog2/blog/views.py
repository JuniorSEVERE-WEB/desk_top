from django.shortcuts import render

# Create your views here.
def blog_list(request):
    return render(request, "list.html")

def post_detail(request):
    return render(request, "detail.html")