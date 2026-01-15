from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Категории')
    description = models.CharField(max_length=300, verbose_name='Описание')


    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ['category_name',]


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=300, verbose_name='Описание')
    picture = models.ImageField(upload_to='picture/', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ['product_name',]
