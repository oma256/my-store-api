from datetime import datetime

from rest_framework.generics import ListAPIView, ListCreateAPIView

from apps.seanses.models import Seanse, Reserve
from apps.seanses.serializers import SeanseSerializer, ReserveSerializer


class SeanseListAPIView(ListAPIView):
    serializer_class = SeanseSerializer
    lookup_field = 'id'

    def get_queryset(self):
        date_object = datetime.strptime(
            self.request.GET.get('date'), '%d-%m-%Y'
        ).date()

        query = Seanse.objects.filter(
            schedule__date=date_object,
            hall__cinema_id=self.request.GET.get('cinema_id'),
        )

        return query


class ReserveListCreateAPIView(ListCreateAPIView):
    serializer_class = ReserveSerializer

    def get_queryset(self):
        print()

        query = Reserve.objects.filter(
            seanse_id=self.kwargs.get('seanse_id'),

        )

        return query
