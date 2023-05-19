from django.test import TestCase

from myapp.models import Course, User
from myapp.Classes.supervisor import Supervisor


# M: As a supervisor I want to be able to create courses, so that I can assign instructors and TAs to courses.


class TestNewCourse(TestCase):
    def setUp(self):
        self.courseList = Course.objects.all()

    # tests that a new course has been created
    def test_new_course_exists(self):
        c = 0
        for course in self.courseList:
            if course.Course_Code == "101":
                c = c + 1
        self.assertTrue(c == 0, "Expected 0 courses, found " + str(c))
        Supervisor.create_course(
            "101", "Intro to Coding", "Learning how to code", "John Doe", "In Person"
        )
        self.courseList = Course.objects.all()
        for course in self.courseList:
            if course.Course_Code == "101":
                c = c + 1
        self.assertTrue(c == 1, "Expected 1 course, found " + str(c))

    # tests that create_course cannot create two courses with same code
    def test_cant_create_duplicates(self):
        Supervisor.create_course(
            "101", "Intro to Coding", "Learning how to code", "John Doe", "In Person"
        )
        Supervisor.create_course(
            "101", "Intro to Coding", "Learning how to code", "John Doe", "In Person"
        )
        c = 0
        self.courseList = Course.objects.all()
        for course in self.courseList:
            if course.Course_Code == "101":
                c = c + 1
        self.assertTrue(c == 1, "Expected 1 course, found " + str(c))

    # tests that create course returns a TypeError on null parameters
    def test_null_code(self):
        result = Supervisor.create_course(
            "", "Intro to Coding", "Learning how to code", "John Doe", "In Person"
        )
        self.assertTrue(
            isinstance(
                result, TypeError), "Expected a type error from create_course"
        )

    def test_null_name(self):
        result = Supervisor.create_course(
            "101", "", "Learning how to code", "John Doe", "In Person")
        self.assertTrue(
            isinstance(
                result, TypeError), "Expected a type error from create_course"
        )

    def test_null_description(self):
        result = Supervisor.create_course(
            "101", "Intro to Coding", "", "John Doe", "In Person")
        self.assertTrue(
            isinstance(
                result, TypeError), "Expected a type error from create_course"
        )
