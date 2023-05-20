from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer

from apps.cinemas.models import Cinema, City, Location, Hall, HallType, Seat


class CitySerializer(ModelSerializer):

    class Meta:
        model = City
        fields = ('id', 'name',)


class LocationSerializer(ModelSerializer):

    class Meta:
        model = Location
        fields = ('id', 'latitude', 'longitude')


class CinemaSerializer(ModelSerializer):
    city = CitySerializer()
    location = LocationSerializer()

    class Meta:
        model = Cinema
        fields = ('id', 'name', 'logo', 'city', 'location')


class HallTypeSerializer(ModelSerializer):

    class Meta:
        model = HallType
        fields = ('id', 'name')


class HallSerializer(ModelSerializer):
    cinema = CinemaSerializer()
    type = HallTypeSerializer()
    seats_count = IntegerField()

    class Meta:
        model = Hall
        fields = ('id', 'name', 'description', 'image',
                  'cinema', 'type', 'seats_count')


class SeatSerializer(ModelSerializer):
    hall = HallSerializer()

    class Meta:
        model = Seat
        fields = ('id', 'row', 'number', 'hall')
