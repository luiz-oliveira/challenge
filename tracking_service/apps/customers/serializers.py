from rest_framework import serializers
from .models import Customer

class CustomerListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Customer
        fields = ('full_name', 'cpf', 'email')

class CustomerDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        exclude = ['id']