import requests

endpoint = "http://127.0.0.1:8000/api/products/"

# 🔹 1. Lire la liste des produits
response = requests.get(endpoint)
print("Produits existants:", response.json())

# 🔹 2. Créer un nouveau produit
new_product = {
    "name": "Tablet",
    "price": "400.00",
    "description": "Une tablette Android"
}
post_response = requests.post(endpoint, json=new_product)
print("Produit créé:", post_response.json())

# 🔹 3. Relire la liste des produits
response = requests.get(endpoint)
print("Nouveaux produits:", response.json())
