import os
import json

from django.shortcuts import render
from mainapp.models import ProductCategory, Product

dir = os.path.dirname(__file__)



def index(request):
    context = {
        'title': 'GeekShop',
        'name_shop': 'GeekShop Store',
        'start_buy': 'Начать покупки',
    }
    return render(request, 'mainapp/index.html', context)

def products(request, pk=None):
    context = {
        'title': 'GeekShop - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
        }
    return render(request, 'mainapp/products.html', context)
