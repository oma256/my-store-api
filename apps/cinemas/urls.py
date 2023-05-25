from django.urls import path

from apps.cinemas.views import (
    CinemaListAPIView, CinemaDetailAPIView, SeatListAPIView, HallListAPIView,
    HallDetailAPIView, SeatDetailAPIView
)


urlpatterns = [
    path('', CinemaListAPIView.as_view(), name='cinema_list'),
    path('<int:cinema_id>',
         CinemaDetailAPIView.as_view(), name='cinema_detail'),
    path('<int:cinema_id>/halls',
         HallListAPIView.as_view(), name='halls_list'),
    path('<int:cinema_id>/halls/<int:hall_id>',
         HallDetailAPIView.as_view(), name='hall_detail'),
    path('<int:cinema_id>/halls/<int:hall_id>/seats',
         SeatListAPIView.as_view(), name='seats_list'),
    path('<int:cinema_id>/halls/<int:hall_id>/seats/<int:seat_id>',
         SeatDetailAPIView.as_view(), name='seat_detail'),
]