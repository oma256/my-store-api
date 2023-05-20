from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.cinemas.models import Cinema
from apps.cinemas.serializers import CinemaSerializer


class CinemaListAPIView(ListAPIView):
    serializer_class = CinemaSerializer
    queryset = Cinema.objects.all()


class CinemaDetailAPIView(RetrieveAPIView):
    serializer_class = CinemaSerializer
    queryset = Cinema.objects.all()
    lookup_field = 'id'
