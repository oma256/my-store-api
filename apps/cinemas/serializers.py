from rest_framework.serializers import ModelSerializer

from apps.cinemas.models import Cinema, City, Location
from apps.seanses.models import Seanse


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


class SeanseSerializer(ModelSerializer):
    class Meta:
        model = Seanse
        fields = ('id', 'movie', 'hall', 'schedule',
                  'price', 'start_time', 'end_time')
