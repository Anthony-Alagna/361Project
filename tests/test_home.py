from django.test import TestCase, Client
from myapp.models import User

# basic unit test for homepage


class HomeTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='secret123')
        self.client.login(username='testuser', password='secret123')

    def test_home_accessible_only_for_authenticated_users(self):
        response = self.client.get("/home/")
        self.assertTrue(self.user.is_authenticated)
        self.assertEqual(response.status_code, 200)
