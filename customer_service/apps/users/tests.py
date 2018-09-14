from rest_framework.test import APITestCase
from rest_framework import status
from oauth2_provider.models import Application, AccessToken
from rest_framework.test import APIRequestFactory, APIClient
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, timedelta



class CustomerTestCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()

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
        

    def _create_authorization_header(self, token=None):
        return "Bearer {0}".format(token or self.access_token.token)

    def test_cannot_access_customer_endpoints_whitout_token(self):
        url = reverse("customers:customers-detail", args=[self.user.pk])  
        response = self.client.post(url)
        self.assertEqual(response.status_code, 401)
