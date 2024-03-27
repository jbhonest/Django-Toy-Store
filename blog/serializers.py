from rest_framework import serializers
from .models import BlogCategory, Post, BlogComment, BlogImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ('id', 'name', 'description')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'category', 'author')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = ('id', 'post', 'text', 'author')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImage
        fields = ('id', 'post', 'caption', 'image')
