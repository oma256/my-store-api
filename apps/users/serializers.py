from rest_framework import serializers
from rest_framework.fields import EmailField, CharField

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')


class UserAuthSerializer(serializers.Serializer):
    email = EmailField(required=True)
    password = CharField(max_length=128, required=True)
