from django.db import models
from django.conf import settings 
from ckeditor.fields import RichTextField


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    content = RichTextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null =True)
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title 
    
class Comment(models.Model):
    posts = models.ForeignKey(Blog,
                              related_name="comments",
                              on_delete=models.CASCADE)    
    name = models.CharField(max_length=300)
    email = models.EmailField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)