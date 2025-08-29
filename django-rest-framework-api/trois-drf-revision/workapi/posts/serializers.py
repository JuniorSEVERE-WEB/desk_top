from rest_framework import serializers
from .models import Post, Comment
from posts.models import Event

class PostSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model = Post 
        fields = ["id", "title", "owner", "owner_username", "content", "created_at"]
        read_only_fields = ["owner", "owner_username"]


class CommentSerializer(serializers.ModelSerializer):
    post_title = serializers.SerializerMethodField(read_only=True)
    author_username = serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model = Comment
        fields = ["id", "post","post_title", "content", "author_username", "created_at", "author"]
        read_only_fields = ["post_title", "author", "author_username"]

    def get_post_title(self, obj):
        return obj.post.title


# EventSerializer déplacé au niveau racine
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event 
        fields = ["id", "title", "description", "date_start", "date_end"]

    def validate_title(self, value):
        if "spam" in value.lower():
            raise serializers.ValidationError("Le titre ne peut pas contenir le mot 'spam'.")
        return value

    def validate(self, data):
        if data["date_start"] >= data["date_end"]:
            raise serializers.ValidationError("La date de fin doit etre superieur apres la date du debut.")
        return data
        

