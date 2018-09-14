"""
    This module contains the debts serializers
"""

from rest_framework import serializers
from .models import Debt

class DebtSerializer(serializers.ModelSerializer):
    """
        Serializes the list of debts
    """
    class Meta:
        model = Debt
        fields = "__all__"
