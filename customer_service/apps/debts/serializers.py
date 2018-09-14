from rest_framework import serializers
from .models import Debt

class DebtSerializer(serializers.ModelSerializer):
    """
        Serializes the debt models
    """  
    class Meta:
        model = Debt
        fields = ("amount", "date_debt")