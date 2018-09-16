"""
    This module contains all patrimony models.
"""

from mongoengine import EmbeddedDocument, fields

class Patrimony(EmbeddedDocument):
    """
        This models contains the patrimony data.
    """
    patrimony_type = fields.StringField(required=True, max_length=100)
    amount = fields.DecimalField(required=True)

    def __str__(self):
        return "{} - R$ {}".format(self.patrimony_type, self.amount)
