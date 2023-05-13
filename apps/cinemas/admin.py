from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.html import format_html

from apps.cinemas.models import Cinema, Location, City, Hall, Seat, HallType


AdminSite.site_header = 'Администрирование CINEMA'


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_logo', 'city', 'location', 'id')

    def get_logo(self, obj):
        return format_html(f'<img src="{obj.logo.url}" width="100" height="70" />')

    get_logo.short_description = 'Фото'


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'get_image', 'type')

    def get_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="100" height="70" />')

    get_image.short_description = 'Фото'


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('row', 'number', 'hall')


@admin.register(HallType)
class HallTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
