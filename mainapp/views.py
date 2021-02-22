from django.shortcuts import render

def index(request):
    return render(request, 'mainapp/index.html')

def products(request):
    return render(request, 'mainapp/products.html')

def test_context(request):
    context = {
    'title': 'geekshop',
    'header': 'Добро пожаловать на сайт!',
    'username': 'Иван Иванов',
    }
    return render(request, 'mainapp/test_context.html', context)
