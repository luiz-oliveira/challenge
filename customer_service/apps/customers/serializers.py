from rest_framework import serializers
from .models import Customer
from apps.debts.serializers import DebtSerializer

class CustomerSerializer(serializers.ModelSerializer):
    """
        Serializes a specific of customers and his debts
    """  
    debts = DebtSerializer(many=True, read_only=True)
    
    class Meta:
        model = Customer
        fields = '__all__'