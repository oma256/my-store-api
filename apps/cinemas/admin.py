from django.contrib import admin

from apps.cinemas.models import Cinema, Location, City


admin.site.register(Cinema)
admin.site.register(Location)
admin.site.register(City)
