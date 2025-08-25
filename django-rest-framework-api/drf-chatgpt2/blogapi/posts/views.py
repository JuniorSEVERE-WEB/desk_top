from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics 
from rest_framework import viewsets 
from django.contrib import admin 



# Create your views here.

#Phase 1 — Chapitre 3 : Serializers (ModelSerializer)
@api_view(['GET'])
def hello_api(request):
    return Response({"message": "Hello from DRF"})

@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


#📚 Phase 1 — Chapitre 4 : CRUD avec les vues génériques
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer     

class CommentListCreateView(generics.ListCreateAPIView)   :
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer 

class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer    


#📚 Phase 1 — Chapitre 5 : ViewSets + Routers (model)
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer     
    






