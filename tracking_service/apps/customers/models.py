from mongoengine import Document, fields
from apps.transactions.models import Transaction

class Customer(Document):
    """
        This models contains the customer data.
    """
    full_name = fields.StringField(max_length=200, required=True)
    cpf = fields.StringField(max_length=11, required=True, unique=True)
    birth_date = fields.DateTimeField(required=True)
    transactions = fields.EmbeddedDocumentListField(Transaction)

    def __str__(self):
        return "{} - {}".format(self.full_name, self.cpf)
