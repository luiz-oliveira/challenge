"""
    This module contains the costumer views
"""

from rest_framework import viewsets
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasScope
from .serializers import CustomerSerializer
from .models import Customer

class CustomerView(viewsets.ModelViewSet):
    """
        A viewset that render a list of customers or a single one
    """

    serializer_class = CustomerSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read', 'write']

    def get_queryset(self):
        """
            This method gets the customers
        """
        customers = Customer.objects.all()
        return self.create_filters(self.request, customers)

    def create_filters(self, request, customers):
        """
            This method filter the customers list
        """
        if request.GET.get("name"):
            customers = customers.filter(full_name__contains=self.request.GET["name"])
        if request.GET.get("cpf"):
            customers = customers.filter(cpf=self.request.GET["cpf"])
        if request.GET.get("email"):
            customers = customers.filter(email=self.request.GET["email"])
        if request.GET.get("phone"):
            customers = customers.filter(email=self.request.GET["phone"])
        return customers
    