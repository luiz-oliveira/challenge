from rest_framework.test import APITestCase
from rest_framework import status
from oauth2_provider.models import Application, AccessToken
from rest_framework.test import APIRequestFactory, APIClient
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class UserTestCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()

        self.csrf_client = APIClient(enforce_csrf_checks=True)
        self.user = User.objects.create_user('user', 'user@gmail.com', 'password')
        self.super_user = User.objects.create_superuser('super_user', 'super_user@gmail.com', 'password')

        # Creating a application to common
        self.app_common = Application.objects.create(
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_PASSWORD,
            redirect_uris='',
            name='common',
            user=self.user
        )

        # Creating a application to common
        self.app_super = Application.objects.create(
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_PASSWORD,
            redirect_uris='',
            name='super',
            user=self.super_user
        )

        # Criating the access token to common_user
        self.access_token_common = AccessToken.objects.create(
            user=self.user,
            scope='read write',
            expires=datetime.now() + timedelta(seconds=300),
            token='secret-access-token-key',
            application=self.app_common
        )

        # Criating the access token to common_user
        self.access_token_super = AccessToken.objects.create(
            user=self.super_user,
            scope='read write',
            expires=datetime.now() + timedelta(seconds=300),
            token='secret-super-access-token-key',
            application=self.app_super
        )

    def _create_authorization_header(self, token=None):
        return "Bearer {0}".format(token or self.access_token_super.token)

    def test_cannot_access_any_endpoint_whitout_token(self):
        url = reverse("customers:customers-list")  
        response = self.csrf_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_cannot_access_user_endpoints_whitout_been_admin(self):
        header = self._create_authorization_header(self.access_token_common)
        url = reverse("users:users-list")  
        response = self.client.get(url, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_list_users(self):
        header = self._create_authorization_header()
        url = reverse("users:users-list")  
        response = self.client.get(url, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_detail_a_user(self):
        header = self._create_authorization_header()
        url = reverse("users:users-detail", args=[self.user.pk])  
        response = self.client.get(url, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)