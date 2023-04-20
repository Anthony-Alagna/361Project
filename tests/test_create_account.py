from django.test import TestCase, Client


# basic unit test for create account page

class CreateAccountTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_account_accessible(self):
        response = self.client.get('/accountbase/createaccount/')
        self.assertEqual(response.status_code, 200)
