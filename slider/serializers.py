from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ModelSerializer
from .models import SliderImage

class SliderImageSerializer(ModelSerializer):
    class Meta:
        model = SliderImage
        fields = '__all__'  # Adjust fields as per your requirements


