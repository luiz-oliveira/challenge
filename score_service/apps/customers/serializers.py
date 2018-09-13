from rest_framework_mongoengine import serializers
from .models import Customer

class CustomerListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Customer
        exclude = ('incomes', 'patrimonies')

class CustomerDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        exclude = ['id']