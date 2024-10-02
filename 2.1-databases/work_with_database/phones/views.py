from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    # Получаем все телефоны из базы данных
    phones = Phone.objects.all()

    # Добавляем их в контекст для передачи в шаблон
    context = {
        'phones': phones
    }

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    # Получаем телефон по slug
    phone = Phone.objects.get(slug=slug)

    # Передаём телефон в шаблон через контекст
    context = {
        'phone': phone
    }

    return render(request, template, context)