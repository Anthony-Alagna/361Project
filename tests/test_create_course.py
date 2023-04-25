import unittest

import django.test
from django.test import TestCase, Client
from myapp.models import User, Course
from myapp.views import CreateCourse
from myapp.Classes.supervisor import Supervisor


# M: As a supervisor I want to be able to create courses, so that I can assign instructors and TAs to courses.


class TestNewCourse(TestCase):
    supervisor = None

    def setUp(self):
        self.supervisor = Client()
        self.courseList = Course.objects.all()
        # self.user1 = User.objects.create(
        #     id='1', User_Name='John Doe', User_Email='user1@example.com',
        #     User_Type='instructor', User_Phone='1234567890', User_Address='123 Main St',
        #     User_LogName='user1', User_LogPass='password', User_isGrader='no',
        #     User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')
        #
        # self.course1 = Course.objects.create(
        #     Course_ID='1', Course_Name='Lion King analysis', Course_Code='382-01',
        #     Course_Instructor=self.user1, Course_isOnline='False',
        #     Course_Location='123 Main St',
        #     User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')

    # tests that a new course has been created
    def test_new_course_exists(self):
        # self.assertTrue(isinstance(Course.objects.get(Course_Code="101"), DoesNotExist), "Expected 0 courses, found 1")
        # result = Supervisor.create_course("101", "Intro to Coding", "Learning how to code", "John Doe")
        # self.assertEqual(result, Course.objects.get(Course_Code="101"), "Expected course with code 101, found none")
        c = 0
        for course in self.courseList:
            if course.Course_Code == "101":
                c = c + 1
        self.assertTrue(c == 0, "Expected 0 courses, found " + str(c))
        Supervisor.create_course("101", "Intro to Coding", "Learning how to code", "John Doe")
        self.courseList = Course.objects.all()
        for course in self.courseList:
            if course.Course_Code == "101":
                c = c + 1
        self.assertTrue(c == 1, "Expected 1 course, found " + str(c))

    # tests that create_course cannot create two courses with same code
    def test_cant_create_duplicates(self):
        Supervisor.create_course("101", "Intro to Coding", "Learning how to code", "John Doe")
        Supervisor.create_course("101", "Intro to Coding", "Learning how to code", "John Doe")
        c = 0
        for course in self.courseList:
            if course.Course_Code == "101":
                c = c + 1
        self.assertTrue(c == 1, "Expected 1 course, found " + str(c))

    # tests that create course returns a TypeError on null parameters
    def test_no_null_parameters(self):
        result = Supervisor.create_course("", "Intro to Coding", "Learning how to code", "John Doe")
        self.assertTrue(isinstance(result, TypeError), "Expected a type error from create_course")
        result = Supervisor.create_course("101", "", "Learning how to code", "John Doe")
        self.assertTrue(isinstance(result, TypeError), "Expected a type error from create_course")
        result = Supervisor.create_course("101", "Intro to Coding", "", "John Doe")
        self.assertTrue(isinstance(result, TypeError), "Expected a type error from create_course")
