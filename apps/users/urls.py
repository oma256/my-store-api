from django.urls import path

from apps.users.views import UserListAPIView, UserDetailAPIView

urlpatterns = [
    path('', UserListAPIView.as_view(), name='users_list'),
    path('<int:id>/', UserDetailAPIView.as_view(), name='user_detail'),
]
