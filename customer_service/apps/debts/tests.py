"""
    This module contains the debit tests
"""

from rest_framework import status
from apps.tests.test_api import CustomAPITestCase

class DebitTestCase(CustomAPITestCase):
    """
        Debit tests cases
    """

    def test_can_create_a_debt(self):
        """
            Test if the user can create a debt
        """
        url = self.reverse_by_name("debts:debts-list")
        payload = {
            "customer_id": self.customer.pk,
            "amount": 2000,
            "date_debt": "2018-08-10",
        }
        response = self.csrf_client.post(url, data=payload, HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_list_debts(self):
        """
            Test if the user can get a list of debts
        """
        url = self.reverse_by_name("debts:debts-list")
        response = self.csrf_client.get(url, HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_detail_a_customer(self):
        """
            Test if the user can get a debt details
        """
        url = self.reverse_by_name("debts:debts-detail", pk=self.debt.pk)
        response = self.csrf_client.get(url, HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_a_customer(self):
        """
            Test if the user can update a debt
        """
        url = self.reverse_by_name("debts:debts-detail", pk=self.debt.pk)
        payload = {"email": "test2@email.com"}
        response = self.csrf_client.patch(url, data=payload, HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_a_customer(self):
        """
            Test if the user can delete a debt
        """
        url = self.reverse_by_name("debts:debts-detail", pk=self.debt.pk)
        response = self.csrf_client.delete(url, HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
