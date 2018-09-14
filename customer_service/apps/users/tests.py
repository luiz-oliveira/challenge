from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User

class ReadCustomerTestCase(TestCase):

    def list_url(self):
        return reverse('users:user-list')

    def detail_url(self):
        return reverse('users:user-detail', args=[self.customer.id])

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

    def test_cannot_read_customer_list_whitout_token(self):
        response = self.client.post(self.list_url())
        self.assertEqual(response.status_code, 401)

    def test_cannot_read_customer_detail_whitout_token(self):
        response = self.client.post(self.list_url())
        self.assertEqual(response.status_code, 401)
