import unittest

from django.test import Client
from django.urls import reverse

from myapp.Classes.users import Users
from myapp.models import User


class UserInformationMethods(unittest.TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            first_name="tester",
            last_name="Smith",
            email="user1@example.com",
            positions="TA",
            phone_number="1234567890",
            address="123 Main St",
            city="Milwaukee",
            password="password14",
            created_at="2022-01-01 00:00:00",
            updated_at="2023-04-18 00:00:00",
        )

    def tearDown(self):
        self.user1.delete()

    def test_get_account_info(self):
        resp = Users.getAccountInfo(self.user1.email, self.user1.id)
        self.assertEqual(resp, self.user1, "Should return the user object")

    def test_get_account_info_unknown_account(self):
        # should raise DoesNotExist error if user doesn't exist
        self.assertRaises(User.DoesNotExist,
                          Users.getAccountInfo, "unknown", 1)

    def test_get_account_missing_parameter(self):
        # should raise DoesNotExist if either argument is blank
        self.assertRaises(User.DoesNotExist, Users.getAccountInfo, "", 1)

    def test_edit_account_info_change_fName(self):
        # Change the firstName
        Users.editInfo(
            self.user1,
            self.user1.phone_number,
            self.user1.address,
            self.user1.city,
            "Bob",
            self.user1.last_name,
        )
        self.assertEqual(
            self.user1.email, "user1@example.com", "email should not have changed"
        )
        self.assertEqual(self.user1.phone_number, "1234567890")
        self.assertEqual(self.user1.last_name, "Smith")
        self.assertEqual(self.user1.address, "123 Main St")
        self.assertEqual(self.user1.city, "Milwaukee")
        self.assertEqual(
            self.user1.first_name, "Bob", "First name should have changed to Bob"
        )

    def test_edit_account_info_change_phone(self):
        # Change the phone number
        Users.editInfo(
            self.user1,
            "1111111111",
            self.user1.address,
            self.user1.city,
            self.user1.first_name,
            self.user1.last_name,
        )
        self.assertEqual(self.user1.email, "user1@example.com")
        self.assertEqual(
            self.user1.phone_number,
            "1111111111",
            "Phone number should have changed to 1111111111",
        )
        self.assertEqual(self.user1.last_name, "Smith")
        self.assertEqual(self.user1.address, "123 Main St")
        self.assertEqual(self.user1.city, "Milwaukee")
        self.assertEqual(
            self.user1.first_name,
            "tester",
        )

    def test_edit_account_info_change_address(self):
        # Change the address
        Users.editInfo(
            self.user1,
            self.user1.phone_number,
            "123 Blvd",
            self.user1.city,
            self.user1.first_name,
            self.user1.last_name,
        )
        self.assertEqual(self.user1.email, "user1@example.com")
        self.assertEqual(self.user1.phone_number, "1234567890")
        self.assertEqual(self.user1.last_name, "Smith")
        self.assertEqual(
            self.user1.address,
            "123 Blvd",
            "Address should have changed to 123 Blvd",
        )
        self.assertEqual(self.user1.city, "Milwaukee")
        self.assertEqual(
            self.user1.first_name,
            "tester",
        )

    def test_edit_account_info_change_position(self):
        # Change the position
        Users.editInfo(
            self.user1,
            self.user1.phone_number,
            self.user1.address,
            self.user1.city,
            self.user1.first_name,
            self.user1.last_name,
            "IN",
        )
        self.assertEqual(self.user1.email, "user1@example.com")
        self.assertEqual(self.user1.phone_number, "1234567890")
        self.assertEqual(self.user1.last_name, "Smith")
        self.assertEqual(self.user1.address, "123 Main St")
        self.assertEqual(self.user1.city, "Milwaukee")
        self.assertEqual(self.user1.first_name, "tester")
        self.assertEqual(
            self.user1.positions, "IN", "Position should have changed to IN"
        )

    def test_edit_account_info_change_city(self):
        # Change the city
        Users.editInfo(self.user1, city="Chicago")
        self.assertEqual(
            self.user1.city, "Chicago", "City should have changed to Chicago"
        )


class PersonalInformationPageTests(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create(
            first_name="tester",
            last_name="Smith",
            email="user1@example.com",
            positions="TA",
            phone_number="1234567890",
            address="123 Main St",
            city="Milwaukee",
            password="password14",
            created_at="2022-01-01 00:00:00",
            updated_at="2023-04-18 00:00:00",
        )

    def tearDown(self):
        self.user1.delete()

    def test_get_edit_personal_information(self):
        url = reverse("personal_information")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_edit_personal_information(self):
        session = self.client.session
        session["username"] = self.user1.email
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
        self.assertEqual(self.user1.first_name, "NewFirstName")
        self.assertEqual(self.user1.last_name, "NewLastName")
        self.assertEqual(self.user1.email, "newemail@example.com")
        self.assertEqual(self.user1.phone_number, "1111111111")
        self.assertEqual(self.user1.address, "New Address")
        self.assertEqual(self.user1.positions, "New Position")
