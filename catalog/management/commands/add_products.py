from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()

    def handle(self, *args, **kwargs):
        group, _ = Category.objects.get_or_create(category_name='Шины', description='Автомобильные колеса')

        products = [
            {'product_name': 'Белшина', 'description': '175/70R13', 'category': group,
             'price': '5500'},
            {'product_name': 'КАМА', 'description': '205/50R15', 'category': group,
             'price': '8500'},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Product added: {product.product_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already added: {product.product_name}'))