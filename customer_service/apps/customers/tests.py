from django.test import TestCase
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
        faker = Faker()

        # Creating a Default user for test
        User.objects.create_superuser('username', 'user@email.com', 'password').save()

        # Login user
        self.client.login(username='john', password='johnpassword')

        # Creating a basic customer
        self.customer = Customer()
        self.customer.full_name = faker.name()
        self.customer.address = faker.address()
        self.customer.cpf = '99999999999'
        self.customer.email = 'test@test.com'
        self.customer.phone = '5524988457899'
        self.customer.save()

    def test_can_read_customer_list(self):
        response = self.client.get(self.list_url())
        self.assertEqual(response.status_code, 200)

    def test_can_read_user_detail(self):
        response = self.client.get(self.detail_url())
        self.assertEqual(response.status_code, 200)
