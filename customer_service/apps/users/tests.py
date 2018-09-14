"""
    This module contains the user tests
"""

from rest_framework import status
from apps.tests.test_api import CustomAPITestCase

class UserTestCase(CustomAPITestCase):
    """
        User tests cases
    """

    def test_cannot_access_any_endpoint_whitout_token(self):
        """
            Test if the user can access an endpoint without a token
        """
        url = self.reverse_by_name("customers:customers-list")
        response = self.csrf_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_cannot_access_user_endpoints_whitout_been_admin(self):
        """
            Test if the user can access users endpoints without been an admin
        """
        url = self.reverse_by_name("users:users-list")
        header = self.create_authorization_header(self.access_token_common)
        response = self.client.get(url, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_list_users(self):
        """
            Test if the user can get a list of users
        """
        url = self.reverse_by_name("users:users-list")
        response = self.client.get(url, HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_detail_a_user(self):
        """
            Test if the user can get a user detais
        """
        url = self.reverse_by_name("users:users-detail", pk=self.user.pk)
        response = self.client.get(url, HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        