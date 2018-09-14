from rest_framework import serializers
from .models import Customer
from apps.debts.serializers import DebtSerializer

class CustomerListSerializer(serializers.ModelSerializer):  
    """
        Serializes a list of customers
    """  
    class Meta:
        model = Customer
        fields = ('full_name', 'cpf', 'email')

class CustomerDetailsSerializer(serializers.ModelSerializer):
    """
        Serializes a specific of customers and his debts
    """  
    debts = DebtSerializer(many=True, read_only=True)
    
    class Meta:
        model = Customer
        exclude = ['id']