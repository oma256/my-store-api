from django.contrib import admin
from django.utils.html import format_html

from apps.seanses.models import Schedule, Seanse, Ticket, Reserve


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('date',)


@admin.register(Seanse)
class SeanseAdmin(admin.ModelAdmin):
    list_display = ('movie', 'hall', 'schedule', 'price',
                    'start_time', 'end_time')


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'get_barcode')

    def get_barcode(self, obj):
        return format_html(f'<img src="{obj.barcode.url}" '
                           f'width="200" height="120" />')

    get_barcode.short_description = 'Баркод'


@admin.register(Reserve)
class ReserveAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'seat', 'seanse')
