from rest_framework import generics
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasScope
from .serializers import CustomerListSerializer, CustomerDetailsSerializer
from .models import Customer

class CustomerList(generics.ListCreateAPIView):
    """
        Renders a list of customers
    """  
    serializer_class = CustomerListSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read', 'write']

    def get_queryset(self):
        customers = Customer.objects.all()
        return self.create_filters(self.request, customers)

    def create_filters(self, request, customers):
        if request.GET.get("name"):
            customers = customers.filter(full_name__contains=self.request.GET["name"])
        if request.GET.get("cpf"):
            customers = customers.filter(cpf=self.request.GET["cpf"])
        if request.GET.get("email"):
            customers = customers.filter(email=self.request.GET["email"])
        if request.GET.get("phone"):
            customers = customers.filter(email=self.request.GET["phone"])
        return customers

class CustomerDetails(generics.RetrieveAPIView):
    """
        Renders a specific customer with his debits
    """  
    queryset = Customer.objects.all()
    serializer_class = CustomerDetailsSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read']
    
    