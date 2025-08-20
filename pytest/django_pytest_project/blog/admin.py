from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Configuration pour l'administration du modèle Post"""
    
    # Colonnes affichées dans la liste des posts
    list_display = ['title', 'published', 'id']
    
    # Filtres disponibles dans la barre latérale
    list_filter = ['published']
    
    # Champs dans lesquels on peut rechercher
    search_fields = ['title', 'content']
    
    # Champs modifiables directement dans la liste
    list_editable = ['published']
    
    # Organisation des champs dans le formulaire d'édition
    fieldsets = (
        ('Contenu du Post', {
            'fields': ('title', 'content')
        }),
        ('Options de publication', {
            'fields': ('published',)
        }),
    )
