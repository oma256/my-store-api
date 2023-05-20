from django.urls import path

from apps.cinemas.views import SeanseListAPIView

urlpatterns = [
    path('', SeanseListAPIView.as_view(), name='seanses_list'),
]