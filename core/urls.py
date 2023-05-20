from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),

    path('api/v1/users/', include('apps.users.urls')),
    path('api/v1/cinemas/', include('apps.cinemas.urls')),
    path('api/v1/movies/', include('apps.movies.urls')),
    path('api/v1/seanses/', include('apps.seanses.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
