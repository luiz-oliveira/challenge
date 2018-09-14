from rest_framework import generics
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasScope
from .serializers import DebtListSerializer, DebtDetailsSerializer
from .models import Debt

class DebtsList(generics.ListCreateAPIView):
    """
        Renders a list of debits
    """  
    queryset = Debt.objects.all()
    serializer_class = DebtListSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read', 'write']


class DebtsDetails(generics.RetrieveAPIView):
    """
        Renders a specific debit with his debits
    """  
    queryset = Debt.objects.all()
    serializer_class = DebtDetailsSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read']
    
    