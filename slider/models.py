from django.db import models
from django.contrib.auth.models import User
    

class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider_images')

    def __str__(self):
        return f"Image for Slider"