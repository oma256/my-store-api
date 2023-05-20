from datetime import datetime

from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.cinemas.models import Cinema
from apps.cinemas.serializers import CinemaSerializer, SeanseSerializer
from apps.seanses.models import Seanse


class CinemaListAPIView(ListAPIView):
    serializer_class = CinemaSerializer
    queryset = Cinema.objects.all()


class CinemaDetailAPIView(RetrieveAPIView):
    serializer_class = CinemaSerializer
    queryset = Cinema.objects.all()
    lookup_field = 'id'


class SeanseListAPIView(ListAPIView):
    serializer_class = SeanseSerializer
    lookup_field = 'id'

    def get_queryset(self):
        print(self.request.GET.get('cinema_id'))
        date_object = datetime.strptime(
            self.request.GET.get('date'), '%d-%m-%Y'
        ).date()

        query = Seanse.objects.filter(schedule__date=date_object)

        return query
