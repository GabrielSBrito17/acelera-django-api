from django.shortcuts import render
from .models import Client, Products, Category
# Create your views here.

def list_products(request):
    products = Products.objects.all()
    return render(request, 'products/list_products.html', {'products': products})