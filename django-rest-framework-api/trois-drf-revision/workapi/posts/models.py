from django.db import models
from django.conf import settings 

# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts", on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.title 
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"Comment on {self.post.title} by {self.author}"
    

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

    def __str__(self):
        return f"Event: {self.title} ({self.date_start:%Y-%m-%d} - {self.date_end:%Y-%m-%d})"

