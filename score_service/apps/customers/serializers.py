"""
    This module contains all customers serializers.
"""

from rest_framework_mongoengine import serializers
from .models import Customer

class CustomerSerializer(serializers.DocumentSerializer):
    """
        Serializes a specific of customers and his incomes / patrimonies
    """
    class Meta:
        model = Customer
        fields = '__all__'
        