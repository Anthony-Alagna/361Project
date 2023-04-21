from django.test import TestCase, Client

# basic unit test for edite account page

class EditAccountTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_edit_account_accessible(self):
        response = self.client.get('/accountbase/editaccount/')
        self.assertEqual(response.status_code, 200)
