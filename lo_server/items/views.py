from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Product
from categories.models import Category
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import  ProductSerializer



@api_view(['GET'])
def products(request):
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    products = Product.objects.filter(is_sold=False)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product(request, pk):
    product = Product.objects.filter(id=pk)
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)



