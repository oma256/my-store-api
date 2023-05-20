from django.urls import path

from apps.seanses.views import SeanseListAPIView, ReserveListCreateAPIView

urlpatterns = [
    path('', SeanseListAPIView.as_view(), name='seanses'),
    path('<int:seanse_id>/reserves', ReserveListCreateAPIView.as_view(), name='reserves'),
]
