from django.test import TestCase, Client
from django.urls import reverse
from myapp.models import User
from myapp.Classes import login
import os

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

    def tearDown(self):
        for i in range(10):
            User.objects.get(email=(i)).delete()

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


class ForgotPasswordTest(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create(
            email=os.getenv("MAIL_USERNAME"),
            User_LogPass=str(1),
        )

    def test_forgot_password_accessible(self):
        """_summary_ tests that the forgot password page is accessible"""
        response = self.client.get(reverse("forgotpassword"))
        self.assertEqual(response.status_code, 200)

    def test_forgot_password_post(self):
        """_summary_ tests that the forgot password form can be submitted"""
        response = self.client.post(
            reverse("forgotpassword"), {"username": os.getenv("MAIL_USERNAME")})
        self.assertEqual(
            response.context["message"], "Password reset email sent")

    def test_forgot_password_post_invalid_username(self):
        """_summary_ tests that an error message is displayed for invalid usernames"""
        response = self.client.post(
            reverse("forgotpassword"), {"username": "invalid"})
        self.assertEqual(
            response.context["message"], "User does not exist, please enter a valid username")

    def test_forgot_password_post_no_username(self):
        """_summary_ tests that an error message is displayed for missing usernames"""
        response = self.client.post(reverse("forgotpassword"), {})
        self.assertEqual(
            response.context["message"], "Please enter a username")


class TestMailClient(TestCase):
    def setUp(self):
        self.testUser = User.objects.create(
            email=os.getenv("MAIL_USERNAME"),
            User_LogPass=str(1),
        )
        self.fp = login.ForgotPassword(
            os.getenv("MAIL_USERNAME"), os.getenv("MAIL_PASSWORD"))

    def tearDown(self):
        self.fp = None

    def test_mail_client(self):
        """_summary_ tests that the mail client can send emails"""
        self.fp.send_reset_email(self.testUser.email)
