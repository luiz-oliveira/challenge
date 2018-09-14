from mongoengine import EmbeddedDocument, fields
from apps.customers.models import Customer

class Transaction(EmbeddedDocument):
    """
        This model contains the transaction data
    """
    amount = fields.DecimalField(max_digits=10, decimal_places=2)
    date_debt = fields.DateField()
    payment_type = fields.CharField(max_length=100)

    def __str__(self):
        return "R$ {} ({})".format(self.amount, self.payment_type)
