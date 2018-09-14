"""
    This module contains the costumer serializers
"""

from rest_framework import serializers
from apps.debts.serializers import DebtSerializer
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    """
        Serializes a specific of customers and his debts
    """
    debts = DebtSerializer(many=True, read_only=True)
    class Meta:
        model = Customer
        fields = '__all__'
