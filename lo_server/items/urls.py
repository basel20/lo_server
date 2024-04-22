from django.urls import path 


from . import views

app_name = 'items'

urlpatterns = [
    path('', views.products, name='products'),
    path('<str:pk>/', views.product, name='product'),
    
]