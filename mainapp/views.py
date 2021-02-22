from django.shortcuts import render

def index(request):
    context = {
        'title': 'GeekShop',
        'name_shop': 'GeekShop Store',
        'start_buy': 'Начать покупки',
    }
    return render(request, 'mainapp/index.html', context)

def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'offer_sheet': ['Новинки', 'Одежда', 'Обувь','Аксессуары', 'Подарки', 'Специальные предложения'],
        }
    return render(request, 'mainapp/products.html', context)
