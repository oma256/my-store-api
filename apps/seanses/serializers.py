from rest_framework.serializers import ModelSerializer

from apps.cinemas.serializers import HallSerializer, SeatSerializer
from apps.movies.serializers import MovieSerializer
from apps.seanses.models import Seanse, Schedule, Ticket, Reserve


class ScheduleSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id', 'date')


class SeanseSerializer(ModelSerializer):
    movie = MovieSerializer()
    hall = HallSerializer()
    schedule = ScheduleSerializer()

    class Meta:
        model = Seanse
        fields = ('id', 'movie', 'hall', 'schedule',
                  'price', 'start_time', 'end_time')


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'uuid', 'barcode')


class ReserveSerializer(ModelSerializer):
    seat = SeatSerializer()
    ticket = TicketSerializer()
    seanse = SeanseSerializer()

    class Meta:
        model = Reserve
        fields = ('seat', 'ticket', 'seanse')
