from django.db import models

class Blogs(models.Model):
    heading = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='preview/', verbose_name='Изображение')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    publication = models.BooleanField(default=True)
    views = models.IntegerField(verbose_name='Просмотры', default=1)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "публикации"
        ordering = ['heading',]
