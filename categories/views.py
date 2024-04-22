from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import  Category
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CategorySerializer



@api_view(['GET'])
def categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

