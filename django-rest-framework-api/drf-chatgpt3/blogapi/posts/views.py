from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

@api_view(['GET'])
def hello_api(request):
    return Response({"message": "Hello from DRF"})

@api_view(['GET'])
def welcome_api(request):
    return Response({"message": "Tu seras un grand developpeur"})

@api_view (['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)
