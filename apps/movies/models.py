from django.db import models

from apps.movies.utils import upload_instance


class Movie(models.Model):
    name = models.CharField(verbose_name='Название', max_length=128)
    description = models.TextField(verbose_name='Описание')
    trailer = models.URLField(verbose_name='Трейлер')
    poster = models.ImageField(verbose_name='Постер', upload_to=upload_instance)

    class Meta:
        verbose_name = 'Фольм',
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.name

