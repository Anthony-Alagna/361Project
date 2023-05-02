import unittest

from django.test import Client
from django.urls import reverse

from myapp.Classes.users import Users
from myapp.models import User


class UserInformationMethods(unittest.TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            User_fName="tester",
            User_lName="Smith",
            User_Email="user1@example.com",
            User_Pos="TA",
            User_Phone="1234567890",
            User_Address="123 Main St",
            User_City="Milwaukee",
            User_LogName="user1ish",
            User_LogPass="password14",
            User_begin="2022-01-01 00:00:00",
            User_Updated="2023-04-18 00:00:00",
        )

    def tearDown(self):
        self.user1.delete()

    def test_get_account_info(self):
        resp = Users.getAccountInfo(self.user1.User_LogName, self.user1.id)
        self.assertEqual(resp, self.user1, "Should return the user object")

    def test_get_account_info_unknown_account(self):
        # should raise DoesNotExist error if user doesn't exist
        self.assertRaises(User.DoesNotExist, Users.getAccountInfo, "unknown", 1)

    def test_get_account_missing_parameter(self):
        # should raise DoesNotExist if either argument is blank
        self.assertRaises(User.DoesNotExist, Users.getAccountInfo, "", 1)

    def test_edit_account_info_change_fName(self):
        # Change the firstName
        Users.editInfo(
            self.user1,
            self.user1.User_Phone,
            self.user1.User_Address,
            self.user1.User_City,
            "Bob",
            self.user1.User_lName,
        )
        self.assertEqual(
            self.user1.User_Email, "user1@example.com", "email should not have changed"
        )
        self.assertEqual(self.user1.User_Phone, "1234567890")
        self.assertEqual(self.user1.User_lName, "Smith")
        self.assertEqual(self.user1.User_Address, "123 Main St")
        self.assertEqual(self.user1.User_City, "Milwaukee")
        self.assertEqual(
            self.user1.User_fName, "Bob", "First name should have changed to Bob"
        )

    def test_edit_account_info_change_phone(self):
        # Change the phone number
        Users.editInfo(
            self.user1,
            "1111111111",
            self.user1.User_Address,
            self.user1.User_City,
            self.user1.User_fName,
            self.user1.User_lName,
        )
        self.assertEqual(self.user1.User_Email, "user1@example.com")
        self.assertEqual(
            self.user1.User_Phone,
            "1111111111",
            "Phone number should have changed to 1111111111",
        )
        self.assertEqual(self.user1.User_lName, "Smith")
        self.assertEqual(self.user1.User_Address, "123 Main St")
        self.assertEqual(self.user1.User_City, "Milwaukee")
        self.assertEqual(
            self.user1.User_fName,
            "tester",
        )

    def test_edit_account_info_change_address(self):
        # Change the address
        Users.editInfo(
            self.user1,
            self.user1.User_Phone,
            "123 Blvd",
            self.user1.User_City,
            self.user1.User_fName,
            self.user1.User_lName,
        )
        self.assertEqual(self.user1.User_Email, "user1@example.com")
        self.assertEqual(self.user1.User_Phone, "1234567890")
        self.assertEqual(self.user1.User_lName, "Smith")
        self.assertEqual(
            self.user1.User_Address,
            "123 Blvd",
            "Address should have changed to 123 Blvd",
        )
        self.assertEqual(self.user1.User_City, "Milwaukee")
        self.assertEqual(
            self.user1.User_fName,
            "tester",
        )

    def test_edit_account_info_change_position(self):
        # Change the position
        Users.editInfo(
            self.user1,
            self.user1.User_Phone,
            self.user1.User_Address,
            self.user1.User_City,
            self.user1.User_fName,
            self.user1.User_lName,
            "IN",
        )
        self.assertEqual(self.user1.User_Email, "user1@example.com")
        self.assertEqual(self.user1.User_Phone, "1234567890")
        self.assertEqual(self.user1.User_lName, "Smith")
        self.assertEqual(self.user1.User_Address, "123 Main St")
        self.assertEqual(self.user1.User_City, "Milwaukee")
        self.assertEqual(self.user1.User_fName, "tester")
        self.assertEqual(
            self.user1.User_Pos, "IN", "Position should have changed to IN"
        )

    def test_edit_account_info_change_city(self):
        # Change the city
        Users.editInfo(self.user1, city="Chicago")
        self.assertEqual(
            self.user1.User_City, "Chicago", "City should have changed to Chicago"
        )

    def test_edit_account_info_change_email(self):
        # Change the email
        Users.editInfo(self.user1, email="test1@test.com")
        self.assertEqual(
            self.user1.User_Email,
            "test1@test.com",
        )


class PersonalInformationPageTests(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create(
            User_fName="tester",
            User_lName="Smith",
            User_Email="user1@example.com",
            User_Pos="TA",
            User_Phone="1234567890",
            User_Address="123 Main St",
            User_City="Milwaukee",
            User_LogName="user1ish",
            User_LogPass="password14",
            User_begin="2022-01-01 00:00:00",
            User_Updated="2023-04-18 00:00:00",
        )

    def tearDown(self):
        self.user1.delete()

    def test_get_edit_personal_information(self):
        url = reverse("personal_information")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_edit_personal_information(self):
        session = self.client.session
        session["username"] = self.user1.User_LogName
        session.save()
        url = reverse("personal_information")
        data = {
            "first_name": "NewFirstName",
            "last_name": "NewLastName",
            "email": "newemail@example.com",
            "phone_number": "1111111111",
            "address": "New Address",
            "position": "New Position",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["success"], "information updated")
        # Refresh the user from the database
        self.user1.refresh_from_db()
        self.assertEqual(self.user1.User_fName, "NewFirstName")
        self.assertEqual(self.user1.User_lName, "NewLastName")
        self.assertEqual(self.user1.User_Email, "newemail@example.com")
        self.assertEqual(self.user1.User_Phone, "1111111111")
        self.assertEqual(self.user1.User_Address, "New Address")
        self.assertEqual(self.user1.User_Pos, "New Position")
