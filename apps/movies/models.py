from django.db import models

from apps.movies.utils import upload_instance


class Movie(models.Model):
    name = models.CharField(verbose_name='Название', max_length=128)
    description = models.TextField(verbose_name='Описание')
    trailer = models.URLField(verbose_name='Трейлер',
                              blank=True, null=True)
    poster = models.ImageField(verbose_name='Постер',
                               upload_to=upload_instance,
                               blank=True, null=True)

    class Meta:
        verbose_name = 'Фильм',
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.name


class MovieGenre(models.Model):
    name = models.CharField(verbose_name='Название', max_length=128)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class MovieDetail(models.Model):
    movie = models.OneToOneField(verbose_name='Фильм',
                                 to=Movie,
                                 on_delete=models.CASCADE)
    premiere = models.DateField(verbose_name='Премьера', null=True, blank=True)
    genre = models.ManyToManyField(verbose_name='Жанр', to=MovieGenre)
    actors = models.CharField(verbose_name='Актеры', max_length=512)

    class Meta:
        verbose_name = 'Детали фильма'
        verbose_name_plural = 'Детали фильмов'

    def __str__(self):
        return f'название: {self.movie.name}, жанр: {self.genre}'
