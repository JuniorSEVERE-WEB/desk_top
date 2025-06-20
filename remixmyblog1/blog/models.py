from django.db import models
from django.conf import settings 
from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    content = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title 


class Comment(models.Model):
    posts = models.ForeignKey(Blog,
                              related_name="comments",
                              on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    name = models.CharField(max_length=200)

    

 