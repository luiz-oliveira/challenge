from rest_framework.test import APITestCase
from rest_framework import status
from oauth2_provider.models import Application, AccessToken
from rest_framework.test import APIRequestFactory, APIClient
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Debt
from apps.customers.models import Customer
from django.utils import timezone
from datetime import timedelta
from faker import Faker


class CustomerTestCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.faker = Faker()

        self.csrf_client = APIClient(enforce_csrf_checks=True)
        self.user = User.objects.create_user('user', 'user@gmail.com', 'password')

        # Creating a application
        self.app = Application.objects.create(
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_PASSWORD,
            redirect_uris='',
            name='dummy',
            user=self.user
        )

        # Criating the access token
        expiration = timezone.now() + timedelta(seconds=300)
        self.access_token = AccessToken.objects.create(
            user=self.user,
            scope='read write',
            expires=expiration,
            token='secret-access-token-key',
            application=self.app
        )

        # Criating a default customer
        self.customer = Customer()
        self.customer.full_name = self.faker.name()
        self.customer.cpf = "98765432198"
        self.customer.email = "customer@customer.com"
        self.customer.phone = "552487996633"
        self.customer.address = self.faker.address()
        self.customer.save()

        # Criating a default debt
        self.debt = Debt()
        self.debt.customer_id = self.customer
        self.debt.amount = 15000
        self.debt.date_debt = "2015-08-18"
        self.debt.save()
        
        # Criating a header
        self.header = self.create_authorization_header()

    def reverse_by_name(self, name, **kwargs):
        return reverse(name, kwargs=kwargs)

    def create_authorization_header(self, token=None):
        return "Bearer {0}".format(token or self.access_token.token)

    def test_can_create_a_debt(self):
        url = self.reverse_by_name("debts:debts-list")
        payload = {
            "customer_id": self.customer.pk,
            "amount": 2000,
            "date_debt": "2018-08-10",
        }
        response = self.csrf_client.post(url, data=payload, HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_list_debts(self):
        url = self.reverse_by_name("debts:debts-list")   
        response = self.csrf_client.get(url, HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_detail_a_customer(self):
        url = self.reverse_by_name("debts:debts-detail", pk=self.debt.pk)
        response = self.csrf_client.get(url, HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_a_customer(self):
        url = self.reverse_by_name("debts:debts-detail", pk=self.debt.pk)
        payload = {"email": "test2@email.com"}      
        response = self.csrf_client.patch(url, data=payload, HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_a_customer(self):
        url = self.reverse_by_name("debts:debts-detail", pk=self.debt.pk)     
        response = self.csrf_client.delete(url, HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
