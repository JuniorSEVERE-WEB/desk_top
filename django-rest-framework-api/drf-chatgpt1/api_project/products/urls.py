from django.urls import path  

from . import views
from .views import ProductAPIView

urlpatterns = [
    #Étape 3 : Créer une vue API simple (JsonResponse)
    path("", views.api_home, name="api_home"),

    #Étape 4 : Echo GET Data
    path("echo/", views.echo_view, name="echo_view"),

    #Étape 5 : Model Instance as API Response
    path("product/", views.product_detail, name="product_detail"),

    #Étape 6 : Model Instance to Dictionary
    path("product-dict/", views.product_dict, name="product_dict"),

    
    #Étape 7 : DRF View & Response
    path('api/drf-product/', ProductAPIView.as_view()),

]
