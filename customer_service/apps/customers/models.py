"""
    This module contains all Customers models.
"""

from django.db import models

class Customer(models.Model):
    """
        This models contains the customer data.
    """
    class Meta:
        indexes = [
            models.Index(fields=['cpf'], name='cpf_index')
        ]

    full_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.full_name, self.cpf)
