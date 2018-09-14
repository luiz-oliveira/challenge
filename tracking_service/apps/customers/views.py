from rest_framework import generics
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasScope
from .serializers import CustomerListSerializer, CustomerDetailsSerializer
from .models import Customer

class CustomerList(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerListSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read']

class CustomerDetails(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerDetailsSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read']
    
    