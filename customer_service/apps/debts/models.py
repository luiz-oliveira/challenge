from django.db import models
from apps.customers.models import Customer

class Debt(models.Model):
    """
        This models contains the debt data.
    """
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='debts')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_debt = models.DateField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} = R$ {}".format(self.customer_id, self.amount)