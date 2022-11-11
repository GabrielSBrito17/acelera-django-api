from django.urls import path
from .views import *

urlpatterns = [
    path('list', list_products, name='list_products')
]