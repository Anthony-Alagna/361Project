from django.test import TestCase, Client
from django.urls import reverse

from myapp.models import Course
from myapp.Classes.supervisor import Supervisor


class TestDeletedCourse(TestCase):
    def setUp(self):
        self.course = Supervisor.create_course(
            "101", "Intro to Coding", "Learning how to code", "John Doe", "In Person"
        )

    def test_course_delete(self):
        Supervisor.delete_course(self.course)
        course_list = Course.objects.all()
        c = 0
        for course in course_list:
            if course.Course_Code == "101":
                c = c + 1
        self.assertTrue(c == 0, "Expected 0 courses, found " + str(c))


class TestButtons(TestCase):
    def test_course_list_page_accessible(self):
        response = self.client.get(reverse("course_base"))
        self.assertEqual(
            response.status_code,
            200,
            "Expected status_code 200, got " + str(response.status_code),
        )
