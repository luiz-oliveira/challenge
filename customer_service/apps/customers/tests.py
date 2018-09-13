from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from .models import Customer
from faker import Faker
from random import randint
from django.contrib.auth.models import User

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


    def test_cannot_read_customer_list_whitout_token(self):
        response = self.client.post(self.list_url())
        self.assertEqual(response.status_code, 401)

    def test_cannot_read_customer_detail_whitout_token(self):
        response = self.client.post(self.list_url())
        self.assertEqual(response.status_code, 401)
