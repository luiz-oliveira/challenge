from rest_framework import serializers
from .models import Debt

class DebtListSerializer(serializers.ModelSerializer):
    """
        Serializes the list of debts
    """  
    class Meta:
        model = Debt
        fields = ("amount", "date_debt")


class DebtDetailsSerializer(serializers.ModelSerializer):
    """
        Serializes a specific of debt
    """
    class Meta:
        model = Debt
        exclude = '__all__'