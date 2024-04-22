from rest_framework.serializers import ModelSerializer
from .models import  Product

from rest_framework.serializers import ModelSerializer
from .models import Product, ProductImage

class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image',)  # Adjust fields as per your requirements

class ProductSerializer(ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
