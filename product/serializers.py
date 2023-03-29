from .models import Category, Product, Review
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name products_count products_list'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id stars text product_title'.split()


class ReviewTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title description price category_n reviews'.split()


class RatingSerializer(serializers.ModelSerializer):
    reviews = ReviewTextSerializer(many=True)

    class Meta:
        model = Product
        fields = 'title reviews rating'.split()


