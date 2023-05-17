from django.test import TestCase, Client
from django.urls import reverse
from myapp.models import User

class ViewAccountTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.user1 = User.objects.create(
            id = 1,
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

    def test_get_personal_information(self):
        id = self.user1.id
        url = reverse("personal_information", kwargs={"id": id})
        data = {
            "firstname": "tester",
            "lastname": "Smith",
            "email": "user1@example.com",
            "password": "password14",
            "address": "123 Main St",
            "city": "Milwaukee",
            "phone_number": "1234567890",
            "position": "TA"
        }
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, 200)
        # Refresh the user from the database
        self.user1.refresh_from_db()
        self.assertEqual(self.user1.User_fName, "tester")
        self.assertEqual(self.user1.User_lName, "Smith")
        self.assertEqual(self.user1.email, "user1@example.com")
        self.assertEqual(self.user1.User_LogPass, "password14")
        self.assertEqual(self.user1.User_Address, "123 Main St")
        self.assertEqual(self.user1.User_City, "Milwaukee")
        self.assertEqual(self.user1.User_Phone, "1234567890")
        self.assertEqual(self.user1.User_Pos, "TA")