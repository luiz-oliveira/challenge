from django.db import models
from apps.customers.models import Customer

class Transaction(models.Model):

    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_debt = models.DateField()
    payment_type = models.CharField(max_length=100)

    def __str__(self):
        return "{} - R$ {} ({})".format(self.customer_id, self.amount, self.payment_type)
