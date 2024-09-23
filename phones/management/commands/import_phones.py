import csv
from django.utils.text import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('phones.csv')

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        for phone in phones:
            for row in phones:
                phone = Phone()
                phone.id = row['id']
                phone.name = row['name']
                phone.image = row['image']
                phone.price = row['price']
                phone.release_date = row['release_date']
                phone.lte_exists = row['lte_exists']
                phone.slug = slugify(row['name'])
                phone.save()

    #для импортирования данных из phoneы.csv в базу данных ввести в терминале команду "python manage.py import_phones phones.csv"


