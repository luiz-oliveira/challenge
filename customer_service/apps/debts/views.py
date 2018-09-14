from rest_framework import viewsets
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasScope
from .serializers import DebtSerializer
from .models import Debt

class DebtView(viewsets.ModelViewSet):
    """
        A viewset that render a list of customers or a single one
    """  
    serializer_class = DebtSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read', 'write']

    def get_queryset(self):
        debts = Debt.objects.all()
        return self.create_filters(self.request, debts)

    def create_filters(self, request, debts):
        if request.GET.get("amount"):
            debts = debts.filter(full_name__contains=self.request.GET["amount"])
        if request.GET.get("date"):
            debts = debts.filter(date_debt=self.request.GET["date"])
        if request.GET.get("cpf"):
            debts = debts.filter(customer_id__cpf=self.request.GET["cpf"])
        return debts
    