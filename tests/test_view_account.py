from django.test import TestCase, Client
from django.urls import reverse
from myapp.models import User


class ViewAccountTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create(
            id=1,
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
        self.user2 = User.objects.create(
            id=2,
            first_name="tester2",
            last_name="Smith2",
            email="user2@example.com",
            positions="TA",
            phone_number="0234567891",
            address="124 Main St",
            city="Milwaukee",
            password="password15",
            created_at="2022-01-02 00:00:00",
            updated_at="2023-04-19 00:00:00",
        )
        self.user3 = User.objects.create(
            id=3,
            first_name="",
            last_name="",
            email="",
            positions="",
            phone_number="",
            address="",
            city="",
            password="",
            created_at="2022-01-02 00:00:00",
            updated_at="2023-04-19 00:00:00",
        )


    def tearDown(self):
        self.user1.delete()
        self.user2.delete()
        self.user3.delete()

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
        self.assertEqual(self.user1.first_name, "tester")
        self.assertEqual(self.user1.last_name, "Smith")
        self.assertEqual(self.user1.email, "user1@example.com")
        self.assertEqual(self.user1.password, "password14")
        self.assertEqual(self.user1.address, "123 Main St")
        self.assertEqual(self.user1.city, "Milwaukee")
        self.assertEqual(self.user1.phone_number, "1234567890")
        self.assertEqual(self.user1.positions, "TA")

    def test_get_others_information(self):
        id = self.user2.id
        url = reverse("personal_information", kwargs={"id": id})
        data = {
            "firstname": "tester2",
            "lastname": "Smith2",
            "email": "user2@example.com",
            "position": "TA"
        }
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, 200)
        # Refresh the user from the database
        self.user2.refresh_from_db()
        self.assertEqual(self.user2.first_name, "tester2")
        self.assertEqual(self.user2.last_name, "Smith2")
        self.assertEqual(self.user2.email, "user2@example.com")
        self.assertEqual(self.user2.positions, "TA")

    def test_blank_information(self):
        id = self.user3.id
        url = reverse("personal_information", kwargs={"id": id})
        data = {
            "firstname": "",
            "lastname": "",
            "email": "",
            "position": ""
        }
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, 200)
        # Refresh the user from the database
        self.user3.refresh_from_db()
        self.assertEqual(self.user3.first_name, "")
        self.assertEqual(self.user3.last_name, "")
        self.assertEqual(self.user3.email, "")
        self.assertEqual(self.user3.positions, "")