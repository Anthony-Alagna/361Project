from django.test import TestCase, Client
from django.urls import reverse

from myapp.models import Course, User
from myapp.Classes.supervisor import Supervisor


class TestButtons(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )

    def tearDown(self):
        self.user.delete()

    def test_course_list_page_accessible(self):
        response = self.client.get(reverse("course_base"))
        self.assertEqual(
            response.status_code,
            200,
            "Expected status_code 200, got " + str(response.status_code),
        )

    def test_new_course_page_accessible(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse("createcourse"))
        self.assertEqual(
            response.status_code,
            200,
            "Expected status_code 200, got " + str(response.status_code),
        )
