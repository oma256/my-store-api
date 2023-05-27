from datetime import datetime

import barcode
from barcode.writer import ImageWriter

from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response

from apps.seanses.models import Seanse, Reserve, Ticket
from apps.seanses.serializers import SeanseSerializer, ReserveSerializer
from core.settings import BASE_DIR, MEDIA_ROOT


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
        query = Reserve.objects.filter(
            seanse_id=self.kwargs.get('seanse_id'),
        )

        return query

    def post(self, *args, **kwargs):
        ticket = Ticket()
        ticket.save()

        ean = barcode.get('ean13', ticket.uuid, writer=ImageWriter())
        ean.save(f'{MEDIA_ROOT}/barcodes/{ticket.uuid}')

        ticket.barcode = f'barcodes/{ticket.uuid}.png'
        ticket.save()

        reserve = Reserve(
            seat_id=self.request.data.get('seat_id'),
            seanse_id=self.request.data.get('seanse_id'),
            ticket_id=ticket.id,
        )
        reserve.save()
        resp_data = self.serializer_class(instance=reserve)

        return Response(data={'status': 'OK', 'data': resp_data.data}, status=201)
