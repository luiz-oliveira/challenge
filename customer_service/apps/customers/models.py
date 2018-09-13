from django.db import models
from .validators import CustomValidators

class Customer(models.Model):

    class Meta:
        indexes = [
            models.Index(fields=['cpf'], name='cpf_index')
        ]

    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField()
    phone = models.CharField(validators=CustomValidators.validate_phone(), max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.full_name, self.cpf)
