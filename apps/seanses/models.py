import barcode
from barcode.writer import ImageWriter
from django.db import models

from apps.cinemas.models import Hall, Seat
from apps.movies.models import Movie
from apps.movies.utils import upload_instance


class Schedule(models.Model):
    date = models.DateField(verbose_name='Дата')

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'

    def __str__(self):
        return f'{self.date}'


class Seanse(models.Model):
    movie = models.ForeignKey(verbose_name='Фильм',
                              to=Movie,
                              on_delete=models.PROTECT)
    hall = models.ForeignKey(verbose_name='Зал',
                             to=Hall,
                             on_delete=models.PROTECT)
    schedule = models.ForeignKey(verbose_name='Расписание',
                                 to=Schedule,
                                 on_delete=models.PROTECT)
    price = models.DecimalField(verbose_name='Цена',
                                max_digits=10,
                                decimal_places=2)
    start_time = models.TimeField(verbose_name='Время начало')
    end_time = models.TimeField(verbose_name='Время конца')

    class Meta:
        verbose_name = 'Сеанс'
        verbose_name_plural = 'Сеансы'

    def __str__(self):
        return f'{self.movie.name} - {self.price}'


class Ticket(models.Model):
    uuid = models.UUIDField(verbose_name='Уникальный UUID')
    barcode = models.ImageField(verbose_name='Баркод',
                                upload_to=upload_instance)

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'

    def generate_barcode_image(self):
        barcode_value = self.uuid
        ean = barcode.get('ean13', barcode_value, writer=ImageWriter())
        image_path = f'{barcode_value}.png'
        ean.save(filename=image_path)
        self.barcode = image_path
        self.save()

    def __str__(self):
        return self.uuid


class Reserve(models.Model):
    seat = models.ForeignKey(verbose_name='Место',
                             to=Seat,
                             on_delete=models.PROTECT)
    ticket = models.OneToOneField(verbose_name='Билет',
                                  to=Ticket,
                                  on_delete=models.PROTECT)
    seanse = models.ForeignKey(verbose_name='Сеанс',
                               to=Seanse,
                               on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'

    def __str__(self):
        return f'место {self.seat.number}, ' \
               f'билет {self.ticket.uuid}, ' \
               f'сеанс: {self.seanse.movie}'
