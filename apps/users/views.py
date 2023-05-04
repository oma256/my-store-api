from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from apps.users.models import User
from apps.users.serializers import UserSerializer


class UserListAPIView(ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailAPIView(RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = UserSerializer
    lookup_field = 'id'
    queryset = User.objects.all()
