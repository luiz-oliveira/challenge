"""
    This module contains the costumer serializers
"""

from rest_framework_mongoengine import serializers
from .models import Customer

class CustomerSerializer(serializers.DocumentSerializer):
    """
        Serializes a specific of customers and his transactions
    """
    class Meta:
        model = Customer
        fields = '__all__'
