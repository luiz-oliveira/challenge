from rest_framework_mongoengine import viewsets
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasScope
from .serializers import CustomerSerializer
from .models import Customer

class Customer(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read', 'write']
    