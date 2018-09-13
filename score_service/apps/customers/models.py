from mongoengine import Document, fields
from apps.incomes.models import Income
from apps.patrimonies.models import Patrimony

class Customer(Document):

    full_name = fields.StringField(max_length=200, required=True)
    cpf = fields.StringField(max_length=11, required=True, unique=True)
    birth_date = fields.DateTimeField(required=True)
    incomes = fields.EmbeddedDocumentListField(Income)
    patrimonies = fields.EmbeddedDocumentListField(Patrimony)

    def __str__(self):
        return "{} - {}".format(self.full_name, self.cpf)
