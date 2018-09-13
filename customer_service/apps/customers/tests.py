from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Customer
from faker import Faker
from random import randint

class ReadCustomerTestCase(TestCase):
    def setUp(self):
    	# Creating a Default user for test
    	self.superuser = User.objects.create_superuser('username', 'user@email.com', 'password')
    	self.superuser.save()

    	# Login user
    	self.client.login(username='john', password='johnpassword')

    	# Creating a basic customer
    	self.customer = Customer()
    	self.customer.full_name = Faker.name()
    	self.customer.address = Faker.address()
    	self.customer.cpf = String(randint(99999999999)) # The CPF is not validated
    	self.customer.email = Faker.ascii_free_email()
    	self.customer.phone = Faker.phone_number()
    	self.customer.save()

    def test_can_read_customer_list(self):
	response = self.client.get(reverse('customer-list'))
	self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_user_detail(self):
        response = self.client.get(reverse('customer-detail', args=[self.customer.id]))
	self.assertEqual(response.status_code, status.HTTP_200_OK)
