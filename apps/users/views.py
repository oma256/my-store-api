from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import NotFound
from rest_framework.generics import (
    GenericAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK

from apps.users.authentication import token_expire_handler, expires_in
from apps.users.models import User
from apps.users.serializers import (
    UserSerializer, UserAuthSerializer, UserCreateSerializer,
)


class UserAuthAPIVIew(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserAuthSerializer

    def post(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.data['email'],
            password=serializer.data['password'],
        )

        if not user:
            return Response(
                data={'detail': 'Invalid Credentials or activate account'},
                status=HTTP_404_NOT_FOUND,
            )

        token, _ = Token.objects.get_or_create(user=user)
        is_expired, token = token_expire_handler(token)
        user_serialized = UserSerializer(user)

        return Response({
            'user': user_serialized.data,
            'expires_in': expires_in(token),
            'token': token.key
        }, status=HTTP_200_OK)


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        self.serializer_class = UserSerializer
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.serializer_class = UserCreateSerializer
        return super().post(request, *args, **kwargs)


class UserDetailDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = UserSerializer
    queryset = User.objects.all()
