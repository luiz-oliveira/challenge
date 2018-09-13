
from mongoengine import EmbeddedDocument, fields

class Patrimony(EmbeddedDocument):

    title = fields.StringField(required=True, max_length=100)
    amount = fields.DecimalField(required=True)

    def __str__(self):
        return "{} - R$ {}".format(self.title, self.amount)
