from rest_framework import serializers
from .models import Customer
from apps.debts.serializers import DebtSerializer

class CustomerListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Customer
        fields = ('full_name', 'cpf', 'email')

class CustomerDetailsSerializer(serializers.ModelSerializer):
    debts = DebtSerializer(many=True, read_only=True)
    
    class Meta:
        model = Customer
        exclude = ['id']