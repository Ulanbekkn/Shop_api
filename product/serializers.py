from .models import Category, Product, Review
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


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


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField()


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    category_id = serializers.IntegerField()

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError(f'Category with id ({category_id}) not found!')
        return category_id


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    product_id = serializers.IntegerField()
    stars = serializers.IntegerField()

    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError(f'Product with id ({product_id}) not found!')
        return product_id





