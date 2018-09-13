from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasScope
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [TokenHasScope, IsAdminUser]
    authentication_classes = [OAuth2Authentication]
    required_scopes = ['read']


class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [TokenHasScope, IsAdminUser]
    authentication_classes = [OAuth2Authentication]
    required_scopes = ['read']