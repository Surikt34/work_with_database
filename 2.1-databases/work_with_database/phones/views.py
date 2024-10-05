from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    # Получаем параметр сортировки из GET-запроса, если он указан
    sort = request.GET.get('sort')

    # Получаем все телефоны
    phones = Phone.objects.all()

    # Применяем сортировку в зависимости от параметра sort
    if sort == 'name':
        phones = phones.order_by('name')  # Сортировка по имени в алфавитном порядке
    elif sort == 'min_price':
        phones = phones.order_by('price')  # Сортировка по цене по возрастанию
    elif sort == 'max_price':
        phones = phones.order_by('-price')  # Сортировка по цене по убыванию

    # Передаём отсортированные телефоны в контекст
    context = {
        'phones': phones,
    }

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    # Получаем телефон по slug
    phone = Phone.objects.get(slug=slug)

    context = {
        'phone': phone
    }

    return render(request, template, context)
