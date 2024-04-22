from django.shortcuts import render
from .models import SliderImage
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SliderImageSerializer
# Create your views here.


@api_view(['GET'])
def sliderImages(request):
    sliderImages = SliderImage.objects.all()
    serializer = SliderImageSerializer(sliderImages, many=True)
    return Response(serializer.data)