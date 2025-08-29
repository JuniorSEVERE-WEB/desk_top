from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .models import Event
from .serializers import EventSerializer

# EventViewSet pour CRUD complet sur Event
from rest_framework import viewsets

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
from rest_framework import generics 
from rest_framework import viewsets, permissions

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

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer    

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer   

class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer     

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer  

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer  



class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Lecture pour tous, écriture réservée au propriétaire de l'objet.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        return getattr(obj, "owner_id", None) == request.user.id

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related("owner").all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, request_serializer):
        # Assigne automatiquement l’owner au user connecté
        request_serializer.save(owner=self.request.user)

    def get_queryset(self):
        # Optionnel : filtrer pour ne retourner que les posts publics ou du user
        return Post.objects.all()

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related("post").all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Si tu veux lier l’auteur au user connecté, assure que Comment a `owner`
        # serializer.save(owner=self.request.user)
        serializer.save()




