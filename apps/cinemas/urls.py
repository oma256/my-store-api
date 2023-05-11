from django.urls import path

from apps.cinemas.views import CinemaListAPIView

urlpatterns = [
    path('', CinemaListAPIView.as_view(), name='cinema_list'),
]