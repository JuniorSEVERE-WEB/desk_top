

# Create your models here.
# nom_de_ton_app/models.py
from django.db import models

class MaSuperModel(models.Model):
    nom = models.CharField(max_length=100)