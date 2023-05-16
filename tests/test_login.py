from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.test import RequestFactory
from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from myapp.models import User
from myapp.Classes.login import ForgotPassword, Logout, ResetPassword
import os

"""_summary_ contains unit tests for the login page
    """


class LoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        for i in range(10):
            User.objects.create(
                email=(i),
                password=str(i),
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

    # def test_login_post_invalid_password(self):
    #     response = self.client.post("", {"username": "1", "password": "2"})
    #     self.assertEqual(response.status_code, 302)
    #
    # def test_login_post_invalid_username(self):
    #     response = self.client.post("", {"username": "2", "password": "1"})
    #     self.assertEqual(response.status_code, 302)
    #
    # def test_login_post_invalid_username_and_password(self):
    #     response = self.client.post("", {"username": "2", "password": "2"})
    #     self.assertEqual(response.status_code, 302)
    #
    # def test_login_post_no_username(self):
    #     response = self.client.post("", {"username": "", "password": "1"})
    #     self.assertEqual(response.status_code, 302)
    #
    # def test_login_post_no_password(self):
    #     response = self.client.post("", {"username": "1", "password": ""})
    #     self.assertEqual(response.status_code, 302)
    #
    # def test_login_post_no_username_and_password(self):
    #     response = self.client.post("", {"username": "", "password": ""})
    #     self.assertEqual(response.status_code, 302)
    #
    # def test_login_post_no_username_and_invalid_password(self):
    #     response = self.client.post("", {"username": "", "password": "2"})
    #     self.assertEqual(response.status_code, 302)


class ForgotPasswordTest(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create(
            email=os.getenv("MAIL_USERNAME"),
            password=str(1),
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
            password=str(1),
        )
        self.fp = ForgotPassword()

    def tearDown(self):
        self.fp = None

    def test_mail_client(self):
        """_summary_ tests that the mail client can send emails"""
        self.assertTrue(self.fp.send_reset_email(self.testUser.email))

    def test_send_email(self):
        # Send message.
        mail.send_mail(
            "Subject here",
            "Here is the message.",
            "from@example.com",
            ["to@example.com"],
            fail_silently=False,
        )

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, "Subject here")


class TestResetPassword(TestCase):
    def setUp(self):
        # Create a test user with a password reset token
        self.user = User.objects.create(
            email="exampleuser@example.com", pw_reset_token="exampleuser@example.com:auth_token", password="old_password")
        self.reset = ResetPassword()

    def tearDown(self):
        self.user.delete()
        self.reset = None

    def test_valid_password_reset(self):
        token = "exampleuser@example.com:auth_token"
        new_password = "new_password123"
        self.assertTrue(self.reset.reset_password(token, new_password))

        # Check that the user's password is updated
        updated_user = User.objects.get(email="exampleuser@example.com")
        self.assertEqual(updated_user.password, new_password)

    def test_invalid_token(self):
        token = "invalid_token"
        new_password = "new_password123"
        with self.assertRaises(ValueError):
            self.reset.reset_password(token, new_password)

    def test_incorrect_auth_string(self):
        token = "exampleuser@example.com:wrong_auth_token"
        new_password = "new_password123"
        self.assertFalse(self.reset.reset_password(token, new_password))

    def test_nonexistent_user(self):
        token = "nonexistentuser:auth_token"
        new_password = "new_password123"
        with self.assertRaises(User.DoesNotExist):
            self.reset.reset_password(token, new_password)

    def test_empty_token(self):
        token = ""
        new_password = "new_password123"
        with self.assertRaises(ValueError, msg="Invalid token"):
            self.reset.reset_password(token, new_password)

    def test_empty_new_password(self):
        token = "exampleuser:auth_token"
        new_password = ""
        with self.assertRaises(ValueError, msg="Token and new password must be provided"):
            self.reset.reset_password(token, new_password)

    def test_valid_password_reset_complex_password(self):
        token = "exampleuser@example.com:auth_token"
        new_password = "C0mpl3x_P@ssw0rd"
        self.assertTrue(self.reset.reset_password(token, new_password))

        # Check that the user's password is updated
        updated_user = User.objects.get(email="exampleuser@example.com")
        self.assertEqual(updated_user.password, new_password)


class LogoutTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(
            email="testuser", password="testpass"
        )

    def test_logout(self):
        path = reverse('logout')
        request = self.factory.get(path)
        login_successful = self.client.login(
            username='testuser', password='testpass')

        if login_successful:
            request.user = self.user
            response = Logout(request).redirect
            self.assertNotIn('user_id', request.session)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, reverse('login'))
            self.assertEqual(response.cookies.get('sessionid').value, '')
        else:
            # Handle the case where login was unsuccessful
            self.fail('Login was unsuccessful')
