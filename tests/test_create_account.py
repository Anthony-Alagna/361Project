from django.test import TestCase, Client
from myapp.models import User


# basic unit test for create account page

class CreateAccountTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_account_accessible(self):
        response = self.client.get('/accountbase/createaccount/')
        self.assertEqual(response.status_code, 200)

    # adds user to the database correctly
    def test_create_account_successful(self):
        result = Supervisor.createAccount("Michael", "Scott", "mscott@uwm.edu", "mscott", "password", "123 Oakland Ave",
                                    "Milwaukee", "4144165289", "Instructor")
        self.assertEqual(result, User.objects.filter(username="mscott"), "Created account not found in database")

    # doesn't add user to the database if username already exists
    def test_create_account_username_exists(self):
        result = Supervisor.createAccount("Michael", "Scott", "mscott@uwm.edu", "mscott", "password", "123 Oakland Ave",
                                    "Milwaukee", "4144165289", "Instructor")
        self.assertNotEqual(result, User.objects.filter(username="mscott"), "Account should not have been created, username already exists")

    # doesn't add user to the database if one of the form field parameters is missing - will redirect back to page with information still filled in

    def test_create_account_field_fname_missing(self):
        result = Supervisor.createAccount("Scott", "mscott@uwm.edu", "mscott", "password", "123 Oakland Ave",
                                "Milwaukee", "4144165289", "Instructor")
        self.assertNotEqual(result, User.objects.filter(User_LogName="mscott"),
                     "Account should not have been created, first name missing")

    def test_create_account_field_lname_missing(self):
        result = Supervisor.createAccount("Michael", "mscott@uwm.edu", "mscott", "password", "123 Oakland Ave",
                                    "Milwaukee", "4144165289", "Instructor")
        self.assertNotEqual(result, User.objects.filter(User_LogName="mscott"),
                         "Account should not have been created, last name missing")

    def test_create_account_field_email_missing(self):
        result = Supervisor.createAccount("Michael", "Scott", "mscott", "password", "123 Oakland Ave",
                                    "Milwaukee", "4144165289", "Instructor")
        self.assertNotEqual(result, User.objects.filter(User_LogName="mscott"),
                         "Account should not have been created, email missing")
    def test_create_account_field_username_missing(self):
        result = Supervisor.createAccount("Michael", "Scott", "mscott@uwm.edu", "password", "123 Oakland Ave",
                                    "Milwaukee", "4144165289", "Instructor")
        self.assertNotEqual(result, User.objects.filter(User_LogPass="password"),
                         "Account should not have been created, username missing")

    def test_create_account_field_password_missing(self):
        result = Supervisor.createAccount("Michael", "Scott", "mscott@uwm.edu", "mscott", "123 Oakland Ave",
                                    "Milwaukee", "4144165289", "Instructor")
        self.assertNotEqual(result, User.objects.filter(User_LogName="mscott"),
                         "Account should not have been created, password missing")

    def test_create_account_field_address_missing(self):
        result = Supervisor.createAccount("Michael", "Scott", "mscott@uwm.edu", "mscott", "password",
                                    "Milwaukee", "4144165289", "Instructor")
        self.assertNotEqual(result, User.objects.filter(User_LogName="mscott"),
                         "Account should not have been created, address missing")

    def test_create_account_field_city_missing(self):
        result = Supervisor.createAccount("Michael", "Scott", "mscott@uwm.edu", "mscott", "password", "123 Oakland Ave",
                                    "4144165289", "Instructor")
        self.assertNotEqual(result, User.objects.filter(User_LogName="mscott"),
                         "Account should not have been created, city missing")

    def test_create_account_field_number_missing(self):
        result = Supervisor.createAccount("Michael", "Scott", "mscott@uwm.edu", "mscott", "password", "123 Oakland Ave",
                                    "Milwaukee", "Instructor")
        self.assertNotEqual(result, User.objects.filter(User_LogName="mscott"),
                         "Account should not have been created, number missing")

    def test_create_account_field_position_missing(self):
        result = Supervisor.createAccount("Michael", "Scott", "mscott@uwm.edu", "mscott", "password", "123 Oakland Ave",
                                    "Milwaukee", "4144165289")
        self.assertNotEqual(result, User.objects.filter(User_LogName="mscott"),
                         "Account should not have been created, position missing")


