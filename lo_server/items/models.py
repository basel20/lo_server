from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
    

class ProductImage(models.Model):
    product = models.ForeignKey('Product', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images')

    def __str__(self):
        return f"Image for {self.product.name}"

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    sizes = models.CharField(max_length=50 , blank=True, null=True)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name

