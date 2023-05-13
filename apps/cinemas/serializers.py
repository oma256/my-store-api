from rest_framework.serializers import ModelSerializer

from apps.cinemas.models import Cinema, City, Location


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
