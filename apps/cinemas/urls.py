from django.urls import path

from apps.cinemas.views import CinemaListAPIView, CinemaDetailAPIView, \
    SeanseListAPIView

urlpatterns = [
    path('', CinemaListAPIView.as_view(), name='cinema_list'),
    path('<int:id>', CinemaDetailAPIView.as_view(), name='cinema_detail'),
]