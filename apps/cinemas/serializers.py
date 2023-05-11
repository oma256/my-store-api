from rest_framework.serializers import ModelSerializer

from apps.cinemas.models import Cinema


class CinemaSerializer(ModelSerializer):

    class Meta:
        model = Cinema
        fields = ('name', 'logo', 'city_id', 'location')
