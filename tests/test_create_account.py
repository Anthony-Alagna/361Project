from django.test import TestCase, Client
from django.urls import reverse

from myapp.models import User
from myapp.Classes.supervisor import Supervisor


# basic unit test for create account page


# Method: Supervisor.create_account(fName: str, lName: str, email: str, username: str, password: str, address: str, city: str, phone: str, account_type: str)
class TestCreateAccount(TestCase):
    def setUp(self):
        self.client = Client()

    # adds user to the database correctly
    def test_create_account_successful(self):
        result = Supervisor.create_account(
            "Michael",
            "Scott",
            "mscott@uwm.edu",
            "mscott",
            "password",
            "123 Oakland Ave",
            "Milwaukee",
            "4144165289",
            "Instructor",
        )
        self.assertEqual(
            result,
            User.objects.get(User_LogName="mscott"),
            "Created account not found in database",
        )

    # doesn't add user to the database if username already exists
    def test_create_account_username_exists(self):
        self.user1 = User.objects.create(
            User_fName="Michael",
            User_lName="Scott",
            User_Email="mscott@uwm.edu",
            User_Pos="Instructor",
            User_Phone="1234567890",
            User_Address="123 Main St",
            User_City="Milwaukee",
            User_LogName="agentscarn",
            User_LogPass="password",
            User_begin="2022-01-01 00:00:00",
            User_Updated="2023-04-18 00:00:00",
        )

        result = Supervisor.create_account(
            "Michael",
            "Scott",
            "mscott@uwm.edu",
            "agentscarn",
            "password",
            "123 Oakland Ave",
            "Milwaukee",
            "4144165289",
            "Instructor",
        )
        self.assertEqual(
            isinstance(result, ValueError),
            True,
            "Account should not have been created, username already exists",
        )

    # doesn't add user to the database if one of the form field parameters is missing
    def test_create_account_field_fname_missing(self):
        result = Supervisor.create_account(
            "",
            "Scott",
            "mscott@uwm.edu",
            "mscott",
            "password",
            "123 Oakland Ave",
            "Milwaukee",
            "4144165289",
            "Instructor",
        )
        self.assertEqual(
            isinstance(result, ValueError),
            True,
            "Account should not have been created, first name missing",
        )

    def test_create_account_field_lname_missing(self):
        result = Supervisor.create_account(
            "Michael",
            "",
            "mscott@uwm.edu",
            "mscott",
            "password",
            "123 Oakland Ave",
            "Milwaukee",
            "4144165289",
            "Instructor",
        )
        self.assertEqual(
            isinstance(result, ValueError),
            True,
            "Account should not have been created, last name missing",
        )

    def test_create_account_field_email_missing(self):
        result = Supervisor.create_account(
            "Michael",
            "Scott",
            "",
            "mscott",
            "password",
            "123 Oakland Ave",
            "Milwaukee",
            "4144165289",
            "Instructor",
        )
        self.assertEqual(
            isinstance(result, ValueError),
            True,
            "Account should not have been created, email missing",
        )

    def test_create_account_field_username_missing(self):
        result = Supervisor.create_account(
            "Michael",
            "Scott",
            "mscott@uwm.edu",
            "",
            "password",
            "123 Oakland Ave",
            "Milwaukee",
            "4144165289",
            "Instructor",
        )
        self.assertEqual(
            isinstance(result, ValueError),
            True,
            "Account should not have been created, username missing",
        )

    def test_create_account_field_password_missing(self):
        result = Supervisor.create_account(
            "Michael",
            "Scott",
            "mscott@uwm.edu",
            "mscott",
            "",
            "123 Oakland Ave",
            "Milwaukee",
            "4144165289",
            "Instructor",
        )
        self.assertEqual(
            isinstance(result, ValueError),
            True,
            "Account should not have been created, password missing",
        )

    def test_create_account_field_address_missing(self):
        result = Supervisor.create_account(
            "Michael",
            "Scott",
            "mscott@uwm.edu",
            "mscott",
            "password",
            "",
            "Milwaukee",
            "4144165289",
            "Instructor",
        )
        self.assertEqual(
            isinstance(result, ValueError),
            True,
            "Account should not have been created, address missing",
        )

    def test_create_account_field_city_missing(self):
        result = Supervisor.create_account(
            "Michael",
            "Scott",
            "mscott@uwm.edu",
            "mscott",
            "password",
            "123 Oakland Ave",
            "",
            "4144165289",
            "Instructor",
        )
        self.assertEqual(
            isinstance(result, ValueError),
            True,
            "Account should not have been created, city missing",
        )

    def test_create_account_field_number_missing(self):
        result = Supervisor.create_account(
            "Michael",
            "Scott",
            "mscott@uwm.edu",
            "mscott",
            "password",
            "123 Oakland Ave",
            "Milwaukee",
            "",
            "Instructor",
        )
        self.assertEqual(
            isinstance(result, ValueError),
            True,
            "Account should not have been created, number missing",
        )

    def test_create_account_field_position_missing(self):
        result = Supervisor.create_account(
            "Michael",
            "Scott",
            "mscott@uwm.edu",
            "mscott",
            "password",
            "123 Oakland Ave",
            "Milwaukee",
            "4144165289",
            "",
        )
        self.assertEqual(
            isinstance(result, ValueError),
            True,
            "Account should not have been created, position missing",
        )

    def test_create_account_accessible(self):
        response = self.client.get(reverse("createaccount"))
        self.assertEqual(response.status_code, 200)
