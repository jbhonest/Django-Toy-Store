from rest_framework import serializers
from .models import Category, Product, Comment, Image


class SimpleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'caption', 'image']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'product', 'text', 'author')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'product', 'caption', 'image')


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all())
    category_info = CategorySerializer(source='category', read_only=True)
    images = SimpleImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description',
                  'price', 'category', 'category_info', 'images')
