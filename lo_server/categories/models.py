from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):  # create a modle 
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to='products_images', blank=True, null=True)

    class Meta:
        ordering = ('name', ) # order the categories Alphabetcaly
        verbose_name_plural = 'Categories'  # Corect the model name
        

    def __str__(self):
        return self.name    # show the value of the items on the admin site
3