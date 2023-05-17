from django.test import TestCase, Client
from django.urls import reverse
from myapp.Classes.users import Users
from myapp.models import User


# Method User.edit_account(first name:str, Last name:str, email:str, password: str, address:str, city:str, phone:str,
# position:str,)
class TestEditAccount(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            User_fName="tester",
            User_lName="Smith",
            email="user1@example.com",
            User_Pos="Teaching Assistant",
            User_Phone="1234567890",
            User_Address="123 Main St",
            User_City="Milwaukee",
            User_LogPass="password14",
            User_begin="2022-01-01 00:00:00",
            User_Updated="2023-04-18 00:00:00",
        )

    def tearDown(self):
        self.user1.delete()

    def test_edit_account_info_change_fName(self):
        # Change the firstName
        Users.edit_account(
            self.user1,
            "Bob",
            self.user1.User_lName,
            self.user1.email,
            self.user1.User_LogPass,
            self.user1.User_Address,
            self.user1.User_City,
            self.user1.User_Phone,
            self.user1.User_Pos
        )
        self.assertEqual(self.user1.email, "user1@example.com", "email should not have changed")
        self.assertEqual(self.user1.User_Phone, "1234567890", "phone number should not have changed")
        self.assertEqual(self.user1.User_lName, "Smith", "last name should not have changed")
        self.assertEqual(self.user1.User_Address, "123 Main St", "address should not have changed")
        self.assertEqual(self.user1.User_City, "Milwaukee", "city should not have changed")
        self.assertEqual(self.user1.User_LogPass, "password14", "password should not have changed")
        self.assertEqual(self.user1.User_fName, "Bob", "First name should have changed to Bob")
        self.assertEqual(self.user1.User_Pos, "Teaching Assistant", "position should not have changed")

    def test_edit_account_info_change_phone(self):
        # Change the phone number
        Users.edit_account(
            self.user1,
            self.user1.User_fName,
            self.user1.User_lName,
            self.user1.email,
            self.user1.User_LogPass,
            self.user1.User_Address,
            self.user1.User_City,
            "1111111111",
            self.user1.User_Pos
        )

        self.assertEqual(self.user1.email, "user1@example.com", "email should not have changed")
        self.assertEqual(self.user1.User_Phone, "1111111111", "Phone number should have changed to 1111111111")
        self.assertEqual(self.user1.User_lName, "Smith", "last name should not have changed")
        self.assertEqual(self.user1.User_Address, "123 Main St", "address should not have changed")
        self.assertEqual(self.user1.User_City, "Milwaukee", "city should not have changed")
        self.assertEqual(self.user1.User_LogPass, "password14", "password should not have changed")
        self.assertEqual(self.user1.User_fName, "tester", "first name should not have changed"
                         )
        self.assertEqual(self.user1.User_Pos, "Teaching Assistant", "position should not have changed")

    def test_edit_account_info_change_address(self):
        # Change the address
        Users.edit_account(
            self.user1,
            self.user1.User_fName,
            self.user1.User_lName,
            self.user1.email,
            self.user1.User_LogPass,
            "123 Blvd",
            self.user1.User_City,
            self.user1.User_Phone,
            self.user1.User_Pos
        )


        self.assertEqual(self.user1.email, "user1@example.com", "email should not have changed")
        self.assertEqual(self.user1.User_Phone, "1234567890", "Phone number should not have changed")
        self.assertEqual(self.user1.User_lName, "Smith", "last name should not have changed")
        self.assertEqual(self.user1.User_Address, "123 Blvd", "Address should have changed to 123 Blvd")
        self.assertEqual(self.user1.User_City, "Milwaukee", "city should not have changed")
        self.assertEqual(self.user1.User_LogPass, "password14", "password should not have changed")
        self.assertEqual(self.user1.User_fName, "tester", "first name should not have changed")
        self.assertEqual(self.user1.User_Pos, "Teaching Assistant", "position should not have changed")

    def test_edit_account_info_change_position(self):
        # Change the position
        Users.edit_account(
            self.user1,
            self.user1.User_fName,
            self.user1.User_lName,
            self.user1.email,
            self.user1.User_LogPass,
            self.user1.User_Address,
            self.user1.User_City,
            self.user1.User_Phone,
            "Instructor",
        )

        self.assertEqual(self.user1.email, "user1@example.com", "email should not have changed")
        self.assertEqual(self.user1.User_Phone, "1234567890", "Phone number should not have changed")
        self.assertEqual(self.user1.User_lName, "Smith", "last name should not have changed")
        self.assertEqual(self.user1.User_Address, "123 Main St", "address should not have changed")
        self.assertEqual(self.user1.User_City, "Milwaukee", "city should not have changed")
        self.assertEqual(self.user1.User_LogPass, "password14", "password should not have changed")
        self.assertEqual(self.user1.User_fName, "tester", "first name should not have changed")
        self.assertEqual(self.user1.User_Pos, "Instructor", "Position should have changed to Instructor")

    def test_edit_account_info_change_city(self):
        # Change the city
        Users.edit_account(self.user1, city="Chicago")

        self.assertEqual(self.user1.email, "user1@example.com", "email should not have changed")
        self.assertEqual(self.user1.User_Phone, "1234567890", "Phone number should not have changed")
        self.assertEqual(self.user1.User_lName, "Smith", "last name should not have changed")
        self.assertEqual(self.user1.User_Address, "123 Main St", "address should not have changed")
        self.assertEqual(self.user1.User_LogPass, "password14", "password should not have changed")
        self.assertEqual(self.user1.User_fName, "tester", "first name should not have changed")
        self.assertEqual(self.user1.User_Pos, "Teaching Assistant", "position should not have changed")
        self.assertEqual(self.user1.User_City, "Chicago", "City should have changed to Chicago")

    def test_edit_account_info_change_email(self):
        # Change the email
        Users.edit_account(self.user1, email="hello@uwm.edu")

        self.assertEqual(self.user1.User_lName, "Smith", "last name should not have changed")
        self.assertEqual(self.user1.User_Phone, "1234567890", "Phone number should not have changed")
        self.assertEqual(self.user1.User_Address, "123 Main St", "address should not have changed")
        self.assertEqual(self.user1.User_LogPass, "password14", "password should not have changed")
        self.assertEqual(self.user1.User_fName, "tester", "first name should not have changed")
        self.assertEqual(self.user1.User_Pos, "Teaching Assistant", "position should not have changed")
        self.assertEqual(self.user1.User_City, "Milwaukee", "city should not have changed")
        self.assertEqual(self.user1.email, "hello@uwm.edu", "Email should have changed to hello@uwm.edu")

    def test_edit_account_info_change_password(self):
        # Change the password
        Users.edit_account(self.user1, password="password")

        self.assertEqual(self.user1.User_Phone, "1234567890", "Phone number should not have changed")
        self.assertEqual(self.user1.User_lName, "Smith", "last name should not have changed")
        self.assertEqual(self.user1.User_Address, "123 Main St", "address should not have changed")
        self.assertEqual(self.user1.User_fName, "tester", "first name should not have changed")
        self.assertEqual(self.user1.User_Pos, "Teaching Assistant", "position should not have changed")
        self.assertEqual(self.user1.User_City, "Milwaukee", "city should not have changed")
        self.assertEqual(self.user1.email, "user1@example.com", "email should not have changed")
        self.assertEqual(self.user1.User_LogPass, "password", "Password should have changed to password")

    def test_edit_account_info_change_lname(self):
        # Change the last name
        Users.edit_account(self.user1, lname="Schrute")

        self.assertEqual(self.user1.User_Phone, "1234567890", "Phone number should not have changed")
        self.assertEqual(self.user1.User_lName, "Schrute", "Last name should have changed to Schrute")
        self.assertEqual(self.user1.User_Address, "123 Main St", "address should not have changed")
        self.assertEqual(self.user1.User_fName, "tester", "first name should not have changed")
        self.assertEqual(self.user1.User_Pos, "Teaching Assistant", "position should not have changed")
        self.assertEqual(self.user1.User_City, "Milwaukee", "city should not have changed")
        self.assertEqual(self.user1.email, "user1@example.com", "email should not have changed")
        self.assertEqual(self.user1.User_LogPass, "password14", "password should not have changed")


class TestButtons(TestCase):
    def setUp(self):
        self.client = Client()

        self.user1 = User.objects.create(
            id=1,
            User_fName="tester",
            User_lName="Smith",
            email="user1@example.com",
            User_Pos="TA",
            User_Phone="1234567890",
            User_Address="123 Main St",
            User_City="Milwaukee",
            User_LogPass="password14",
            User_begin="2022-01-01 00:00:00",
            User_Updated="2023-04-18 00:00:00",
        )

    def tearDown(self):
        self.user1.delete()

    def test_edit_account_accessible(self):
        id = self.user1.id
        url = reverse("editaccount", kwargs={"id": id})
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_post_edit_account(self):
        id = self.user1.id
        url = reverse("editaccount", kwargs={"id": id})
        data = {
            "firstname": "NewFirstName",
            "lastname": "NewLastName",
            "email": "newemail@example.com",
            "password": "newpassword",
            "address": "New Address",
            "city": "New City",
            "phone_number": "9876543210",
            "position": "Professor"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        # Refresh the user from the database
        self.user1.refresh_from_db()
        self.assertEqual(self.user1.User_fName, "NewFirstName")
        self.assertEqual(self.user1.User_lName, "NewLastName")
        self.assertEqual(self.user1.email, "newemail@example.com")
        self.assertEqual(self.user1.User_LogPass, "newpassword")
        self.assertEqual(self.user1.User_Address, "New Address")
        self.assertEqual(self.user1.User_City, "New City")
        self.assertEqual(self.user1.User_Phone, "9876543210")
        self.assertEqual(self.user1.User_Pos, "Professor")

