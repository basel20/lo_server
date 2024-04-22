from django.contrib import admin

from .models import  Product, ProductImage  # Import your model

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_sold')
    list_filter = ('category',) 
    search_fields = ('name',)
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin ) 
admin.site.register(ProductImage ) 
