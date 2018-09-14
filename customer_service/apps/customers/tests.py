from rest_framework.test import APITestCase
from rest_framework import status
from oauth2_provider.models import Application, AccessToken
from rest_framework.test import APIRequestFactory, APIClient
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Customer
from datetime import datetime, timedelta
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
        self.access_token = AccessToken.objects.create(
            user=self.user,
            scope='read write',
            expires=datetime.now() + timedelta(seconds=300),
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
        

    def _create_authorization_header(self, token=None):
        return "Bearer {0}".format(token or self.access_token.token)

    def test_can_create_customer(self):
        header = self._create_authorization_header()
        url = reverse("customers:customers-list")
        payload = {
            "full_name": self.faker.name(),
            "address": self.faker.address(),
            "cpf": "12345678912",
            "email": "test@email.com",
            "phone": "5524988745211"
        }
        
        response = self.csrf_client.post(url, data=payload, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_list_customers(self):
        header = self._create_authorization_header()
        url = reverse("customers:customers-list")       
        response = self.csrf_client.get(url, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_detail_a_customer(self):
        header = self._create_authorization_header()
        url = reverse("customers:customers-detail", args=[self.customer.pk])       
        response = self.csrf_client.get(url, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_a_customer(self):
        header = self._create_authorization_header()
        url = reverse("customers:customers-list")
        payload = {"email": "test2@email.com"}

        url = reverse("customers:customers-detail", args=[self.customer.pk])       
        response = self.csrf_client.patch(url, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_a_customer(self):
        header = self._create_authorization_header()
        url = reverse("customers:customers-detail", args=[self.customer.pk])       
        response = self.csrf_client.delete(url, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
