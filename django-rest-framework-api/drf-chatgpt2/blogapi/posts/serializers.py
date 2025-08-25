from rest_framework import serializers 
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ['id', 'title', 'content', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    post_title = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Comment
        fields = ["id", "post", "post_title", "content", "created_at", "author"]

    def get_post_title(self, obj):
        return obj.post.title     
