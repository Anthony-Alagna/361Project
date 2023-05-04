from django.test import TestCase, Client
from myapp.models import User

"""_summary_ contains unit tests for the login page
    """


class LoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        for i in range(10):
            User.objects.create(
                email=(i),
                User_LogPass=str(i),
            )

    def test_login_accessible(self):
        """_summary_ tests that the login page is accessible"""
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)

    def test_login_post(self):
        """_summary_ tests that the login page redirects to the home page"""
        response = self.client.post("", {"username": "1", "password": "1"})
        self.assertRedirects(response, "/home/")

    def test_login_post_invalid_password(self):
        response = self.client.post("", {"username": "1", "password": "2"})
        self.assertEqual(response.status_code, 302)

    def test_login_post_invalid_username(self):
        response = self.client.post("", {"username": "2", "password": "1"})
        self.assertEqual(response.status_code, 302)

    def test_login_post_invalid_username_and_password(self):
        response = self.client.post("", {"username": "2", "password": "2"})
        self.assertEqual(response.status_code, 302)

    def test_login_post_no_username(self):
        response = self.client.post("", {"username": "", "password": "1"})
        self.assertEqual(response.status_code, 302)

    def test_login_post_no_password(self):
        response = self.client.post("", {"username": "1", "password": ""})
        self.assertEqual(response.status_code, 302)

    def test_login_post_no_username_and_password(self):
        response = self.client.post("", {"username": "", "password": ""})
        self.assertEqual(response.status_code, 302)

    def test_login_post_no_username_and_invalid_password(self):
        response = self.client.post("", {"username": "", "password": "2"})
        self.assertEqual(response.status_code, 302)
