from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, get_object_or_404,
)

from apps.cinemas.models import Cinema, Seat, Hall
from apps.cinemas.serializers import CinemaSerializer, SeatSerializer, \
    HallSerializer


class CinemaListAPIView(ListAPIView):
    serializer_class = CinemaSerializer
    queryset = Cinema.objects.all()


class CinemaDetailAPIView(RetrieveAPIView):
    serializer_class = CinemaSerializer
    queryset = Cinema.objects.all()
    lookup_field = 'cinema_id'


class HallListAPIView(ListAPIView):
    serializer_class = HallSerializer

    def get_queryset(self):
        return Hall.objects.filter(cinema_id=self.kwargs.get('cinema_id'))


class HallDetailAPIView(RetrieveAPIView):
    serializer_class = HallSerializer

    def get_object(self):
        cinema = get_object_or_404(Cinema,
                                   id=self.kwargs.get('cinema_id'))
        hall = get_object_or_404(Hall,
                                 id=self.kwargs.get('hall_id'),
                                 cinema_id=cinema.id)

        return hall


class SeatListAPIView(ListAPIView):
    serializer_class = SeatSerializer

    def get_queryset(self):
        cinema = get_object_or_404(Cinema,
                                   id=self.kwargs.get('cinema_id'))
        hall = get_object_or_404(Hall,
                                 id=self.kwargs.get('hall_id'),
                                 cinema_id=cinema.id)
        seats = Seat.objects.filter(hall_id=hall.id)

        return seats


class SeatDetailAPIView(RetrieveAPIView):
    serializer_class = SeatSerializer

    def get_object(self):
        cinema = get_object_or_404(Cinema,
                                   id=self.kwargs.get('cinema_id'))
        hall = get_object_or_404(Hall,
                                 id=self.kwargs.get('hall_id'),
                                 cinema_id=cinema.id)
        seat = get_object_or_404(Seat,
                                 id=self.kwargs.get('seat_id'),
                                 hall_id=hall.id)

        return seat
