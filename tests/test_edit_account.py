from django.test import TestCase, Client
from django.urls import reverse


class TestEditAccount(TestCase):
    def setUp(self):
        self.client = Client()

    def test_edit_account_accessible(self):
        response = self.client.get(reverse("accountbase"))
        self.assertEqual(response.status_code, 200)
