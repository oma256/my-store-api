from rest_framework.generics import ListAPIView

from apps.cinemas.models import Cinema
from apps.cinemas.serializers import CinemaSerializer


class CinemaListAPIView(ListAPIView):
    serializer_class = CinemaSerializer
    queryset = Cinema.objects.all()
