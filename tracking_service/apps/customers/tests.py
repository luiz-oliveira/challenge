"""
    This module contains the customers tests
"""

from rest_framework import status
from apps.tests.test_api import CustomAPITestCase

class CustomerTestCase(CustomAPITestCase):
    """
        Customer tests cases
    """

    def test_can_list_customers(self):
        """
            Test if the user can a list of customers
        """
        url = self.reverse_by_name("customers:customers-list")
        response = self.csrf_client.get(url, HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_detail_a_customer(self):
        """
            Test if the user can get a customer details
        """
        url = self.reverse_by_name("customers:customers-detail", pk=self.customer.id)
        response = self.csrf_client.get(url, HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_a_customer(self):
        """
            Test if the user can delete a customer
        """
        url = self.reverse_by_name("customers:customers-detail", pk=self.customer.id)
        response = self.csrf_client.delete(url, HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
