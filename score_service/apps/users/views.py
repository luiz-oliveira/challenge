"""
    This module contains all the users views
"""

from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasScope
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserList(generics.ListAPIView):
    """
        Renders a list of users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [TokenHasScope, IsAdminUser]
    authentication_classes = [OAuth2Authentication]
    required_scopes = ['read', 'write']

class UserDetails(generics.RetrieveAPIView):
    """
        Renders a specific user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [TokenHasScope, IsAdminUser]
    authentication_classes = [OAuth2Authentication]
    required_scopes = ['read', 'write']
