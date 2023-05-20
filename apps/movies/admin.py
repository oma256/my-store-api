from django.contrib import admin
from django.utils.html import format_html

from apps.movies.models import Movie, MovieGenre, MovieDetail


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'trailer', 'get_poster')

    def get_poster(self, obj):
        print(obj.poster.url)
        return format_html(f'<img src="{obj.poster.url}" '
                           f'width="70" height="100" />')

    get_poster.short_description = 'Постер'


@admin.register(MovieGenre)
class MovieGenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(MovieDetail)
class MovieDetailAdmin(admin.ModelAdmin):
    list_display = ('movie', 'premiere', 'actors', 'get_genre')

    def get_genre(self, obj):
        return '\n'.join([g.name for g in obj.genre.all()])

    get_genre.short_description = 'Жанр'
