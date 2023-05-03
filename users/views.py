from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User


class UserListView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        emails = [user.email for user in User.objects.all()]

        return Response(emails)
