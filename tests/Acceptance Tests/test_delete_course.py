from django.test import TestCase, Client
from django.urls import reverse

from myapp.models import Course, User
from myapp.Classes.supervisor import Supervisor


class TestButtons(TestCase):
    def test_course_list_page_accessible(self):
        response = self.client.get(reverse("course_base"))
        self.assertEqual(
            response.status_code,
            200,
            "Expected status_code 200, got " + str(response.status_code),
        )
