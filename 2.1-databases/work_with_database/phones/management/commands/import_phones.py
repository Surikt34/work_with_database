import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass  # Пока аргументы не требуются

    def handle(self, *args, **options):
        # Открываем файл с данными
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        # Проходим по каждому телефону из файла
        for phone in phones:
            # Обрабатываем поле lte_exists
            lte_exists = phone['lte_exists'].strip().lower() in ['true', '1']

            # Добавляем сохранение модели
            phone_obj = Phone(
                name=phone['name'],
                price=phone['price'],
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=lte_exists,  # Используем обработанное значение
                slug=slugify(phone['name'])  # Генерируем slug на основе имени
            )
            phone_obj.save()

        self.stdout.write(self.style.SUCCESS('Phones imported successfully'))


