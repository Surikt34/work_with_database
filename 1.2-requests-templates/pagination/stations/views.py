from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.shortcuts import render
from django.core.paginator import Paginator
from django.conf import settings

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # Читаем CSV-файл
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        stations = list(reader)

    # Пагинация: количество элементов на страницу
    paginator = Paginator(stations, 10)  # 10 станций на страницу

    # Получаем текущую страницу из GET-запроса (по умолчанию страница 1)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    # Формируем контекст для передачи в шаблон
    context = {
        'bus_stations': page,  # Страницы и данные о станциях
        'page': page,  # Текущая страница
    }

    return render(request, 'stations/index.html', context)
