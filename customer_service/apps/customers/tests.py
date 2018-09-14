from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from .models import Customer
from apps.debts.models import Debt
from faker import Faker
from django.contrib.auth.models import User
from datetime import date

class ReadCustomerTestCase(TestCase):

    def list_url(self):
        return reverse('customers:customer-list')

    def detail_url(self):
        return reverse('customers:customer-detail', args=[self.customer.id])

    def setUp(self):
        self.faker = Faker()
        self.client = Client()
        self.factory = RequestFactory()

        # Creating a super_user
        self.super_user = User.objects.create_superuser('username', 'user@email.com', 'password').save()

        # Creating a basic customer
        self.customer = Customer()
        self.customer.full_name = self.faker.name()
        self.customer.address = self.faker.address()
        self.customer.cpf = '99999999999'
        self.customer.email = 'test@test.com'
        self.customer.phone = '5524988457899'
        self.customer.save()

        # Creating a basic debit
        self.debit = Debt()
        self.debit.customer_id = self.customer
        self.debit.amount = 1000
        self.debit.date_debt = date.today()
        self.debit.save()
