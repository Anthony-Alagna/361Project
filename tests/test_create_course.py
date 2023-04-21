from django.test import TestCase, Client
from myapp.models import User, Course
from myapp.views import InstructorToCourse


# M: As a supervisor I want to be able to create courses, so that I can assign instructors and TAs to courses.


# class TestNewCourse(TestCase):
#     def setUp(self):
#
#     def test_course_in_database(self):
