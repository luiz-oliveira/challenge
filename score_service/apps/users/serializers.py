"""
    This module contains the users serializers
"""

from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    """
        Serializes the user models
    """
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")
        