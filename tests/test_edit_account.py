import self as self
from django.test import TestCase, Client
from django.urls import reverse

from myapp.models import User


# Method Supervisor.edit_account(first name:str, Last name:str, email:str, password: str, address:str, city:str, phone:str, position:str,)
class TestEditAccount(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            id="1",
            User_fName="Cricket",
            User_lName="Maule",
            email="user1@example.com",
            User_Pos="Teaching Assistant",
            User_Phone="1234567890",
            User_Address="123 Main St",
            User_City="Milwaukee",
            User_LogPass="password",
            User_begin="2022-01-01 00:00:00",
            User_Updated="2023-04-18 00:00:00",
        )

    def tearDown(self):
        self.user1.delete()


class TestButtons(TestCase):
    def setUp(self):
        self.client = Client()

    def test_edit_account_accessible(self):
        response = self.client.get(reverse("accountbase"))
        self.assertEqual(response.status_code, 200)
