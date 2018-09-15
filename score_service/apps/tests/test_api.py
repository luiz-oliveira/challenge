"""
    This module defines the common test setups
"""

from datetime import timedelta
from oauth2_provider.models import Application, AccessToken
from rest_framework.test import APIRequestFactory, APIClient, APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from faker import Faker
from apps.customers.models import Customer
from test_addons import MongoTestCase


class CustomAPITestCase(APITestCase, MongoTestCase):
    """
        Custom API setup that extends of APITestCase and
        implements some methods used on all apps.
    """

    CLEAR_CACHE = True

    def setUp(self):
        """
            Setup the test case
        """
        self.factory = APIRequestFactory()
        self.faker = Faker()
        self.csrf_client = APIClient(enforce_csrf_checks=True)
        # Creating a common user
        self.user = User.objects.create_user(
            'user',
            'user@gmail.com',
            'password'
        )
        # Creating a super user
        self.super_user = User.objects.create_superuser(
            'super_user',
            'super_user@gmail.com',
            'password'
        )

        # Creating a application to common_user
        app_common = Application.objects.create(
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_PASSWORD,
            redirect_uris='',
            name='common',
            user=self.user
        )

        # Creating a application to super_user
        app_super = Application.objects.create(
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
            expires=timezone.now() + timedelta(seconds=300),
            token='secret-access-token-key',
            application=app_common
        )

        # Criating the access token to super_user
        self.access_token_super = AccessToken.objects.create(
            user=self.super_user,
            scope='read write',
            expires=timezone.now() + timedelta(seconds=300),
            token='secret-super-access-token-key',
            application=app_super
        )

        # Criating a header
        self.header = self.create_authorization_header()

        # Criating a default customer
        self.customer = Customer()
        self.customer.full_name = self.faker.name()
        self.customer.cpf = "45678524155"
        self.customer.birth_date = "2000-11-11"
        self.customer.save()

    def reverse_by_name(self, name, **kwargs):
        """
            Get the url revesed by name
        """
        return reverse(name, kwargs=kwargs)

    def create_authorization_header(self, token=None):
        """
            Get the header with authentication token
        """
        return "Bearer {0}".format(token or self.access_token_super.token)
