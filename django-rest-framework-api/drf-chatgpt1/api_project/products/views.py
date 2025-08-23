from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
#Étape 3 : Créer une vue API simple (JsonResponse)
def api_home(request):
    return JsonResponse({ "message": "Hello, world!" })

#Étape 4 : Echo GET Data
def echo_view(request):
    data = request.GET
    return JsonResponse({"You_sent": dict(data)})

#Étape 5 : Model Instance as API Response
def product_detail(request):
    obj = Product.objects.first()  # prend le premier produit
    data = {
        "id": obj.id,
        "name": obj.name,
        "price": str(obj.price),  # JSON n'accepte pas Decimal directement
    }
    return JsonResponse(data)

#Étape 6 : Model Instance to Dictionary
def product_dict(request):
    obj = Product.objects.first()
    data = model_to_dict(obj)
    return JsonResponse(data)

#Étape 7 : DRF View & Response
class ProductAPIView(APIView):
    def get(self, request):
        obj = Product.objects.first()
        data = {
            "id": obj.id,
            "name": obj.name,
            "price": str(obj.price),
        }
        return Response(data)

