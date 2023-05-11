from django.db import models
from apps.movies.utils import upload_instance


class City(models.Model):
    name = models.CharField(verbose_name='Название', max_length=128)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class Location(models.Model):
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return f'Широта: {self.latitude} - Долгота: {self.longitude}'


class Cinema(models.Model):
    name = models.CharField(verbose_name='Название', max_length=128)
    logo = models.ImageField(verbose_name='Лого', upload_to=upload_instance)
    city = models.ForeignKey(to='City',
                             on_delete=models.SET_NULL,
                             related_name='cinemas',
                             null=True)
    location = models.ForeignKey(to='Location',
                                 on_delete=models.SET_NULL,
                                 related_name='cinemas',
                                 null=True)

    class Meta:
        verbose_name = 'Кинотеатр'
        verbose_name_plural = 'Кинотеатры'

    def __str__(self):
        return self.name


class HallType(models.Model):
    name = models.CharField(verbose_name='Название', max_length=128)

    class Meta:
        verbose_name = 'Тип зала'
        verbose_name_plural = 'Типы залов'

    def __str__(self):
        return self.name


class Hall(models.Model):
    name = models.CharField(verbose_name='Зал', max_length=255)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Фото', upload_to=upload_instance)
    cinema = models.ForeignKey(to='Cinema',
                               on_delete=models.CASCADE,
                               related_name='halls')
    type = models.ForeignKey(to='HallType',
                             on_delete=models.SET_NULL,
                             null=True)

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'

    def __str__(self):
        return self.name


class Seat(models.Model):
    row = models.PositiveSmallIntegerField(verbose_name='Ряд')
    number = models.PositiveSmallIntegerField(verbose_name='Место')
    hall = models.ForeignKey(to='Hall',
                             on_delete=models.CASCADE,
                             related_name='seats')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return f'Ряд: {self.row}, Место {self.number}'
