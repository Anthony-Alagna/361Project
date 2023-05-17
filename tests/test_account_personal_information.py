from unittest import TestCase
from django.test import Client
from django.urls import reverse
from myapp.models import User


class PersonalInformationPageTests(TestCase):

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
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    #click edit button
    def test_go_edit_account(self):
        id = self.user1.id
        url = reverse("editaccount", kwargs={"id": id})
        print(url)
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

