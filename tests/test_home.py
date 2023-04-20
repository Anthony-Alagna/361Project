from django.test import TestCase, Client

# basic unit test for homepage

class HomeTest(TestCase):
    def setUp(self):
        self.client = Client()
    def test_home_accessible(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
