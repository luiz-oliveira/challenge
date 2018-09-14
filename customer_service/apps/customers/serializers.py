from rest_framework import serializers
from .models import Customer
from apps.debts.serializers import DebtListSerializer

class CustomerListSerializer(serializers.ModelSerializer):  
    """
        Serializes a list of customers
    """  
    class Meta:
        model = Customer
        fields = ('id','full_name', 'cpf', 'email')

class CustomerDetailsSerializer(serializers.ModelSerializer):
    """
        Serializes a specific of customers and his debts
    """  
    debts = DebtListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Customer
        exclude = ['id']