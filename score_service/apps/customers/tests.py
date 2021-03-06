"""
    This module contains the customers tests
"""

from rest_framework import status
from apps.tests.test_api import CustomAPITestCase

class CustomerTestCase(CustomAPITestCase):
    """
        Customer tests cases
    """

    def test_can_create_a_customer(self):
        """
            Test if the user can create a customer
        """
        url = self.reverse_by_name("customers:customers-list")
        payload = {
            "full_name": self.faker.name(),
            "cpf": "12345678912",
            "birth_date": "1992-04-10 00:00:00",
            "incomes": [],
            "patrimonies": []
        }
        response = self.csrf_client.post(url, data=payload, HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

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
        url = self.reverse_by_name("customers:customers-detail", id=self.customer.id)
        response = self.csrf_client.get(url, HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_a_customer(self):
        """
            Test if the user can update a customer
        """
        url = self.reverse_by_name("customers:customers-detail", id=self.customer.pk)
        payload = {"birth_date": "1992-04-10 10:01:00"}
        response = self.csrf_client.patch(url, data=payload, HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_a_customer(self):
        """
            Test if the user can delete a customer
        """
        url = self.reverse_by_name("customers:customers-detail", id=self.customer.id)
        response = self.csrf_client.delete(url, HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
