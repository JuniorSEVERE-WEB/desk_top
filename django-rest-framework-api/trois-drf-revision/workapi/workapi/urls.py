"""
URL configuration for workapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from posts.views import hello_api, welcome_api
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet, CommentViewSet, EventViewSet
from posts.views import hello_api, welcome_api, post_list, comment_list, PostListCreateView, PostRetrieveUpdateDestroyView, CommentListCreateView, CommentRetrieveUpdateDestroyView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename="post") 
router.register(r'comments', CommentViewSet, basename="comment")
router.register(r'events', EventViewSet, basename="event")
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/hello/", hello_api),
    path("api/welcome/", welcome_api),
    path("api/posts-old/", post_list),
    path("api/comments-old/", comment_list),
    #path("api/posts/", PostListCreateView.as_view()),
    #path("api/posts/<int:pk>/", PostRetrieveUpdateDestroyView.as_view()),
    #path("api/comments/", CommentListCreateView.as_view()),
    #path("api/comments/<int:pk>/", CommentRetrieveUpdateDestroyView.as_view()),
    path("api/", include(router.urls)),
    path("api/auth/jwt/create/", TokenObtainPairView.as_view(), name="jwt-create"),   # email/username + password
    path("api/auth/jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),

    
]
