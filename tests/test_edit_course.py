from django.test import TestCase, Client
from django.urls import reverse

from myapp.models import Course
from myapp.Classes.supervisor import Supervisor


# S: As a supervisor, I want to be able to edit courses, so that I can update a course's information if it changes


class TestEditedCourse(TestCase):
    def setUp(self):
        self.course = Supervisor.create_course(
            "101", "Intro to Coding", "Learning how to code", "John Doe", "In Person"
        )

    def test_edit_code(self):
        Supervisor.edit_course(self.course, "102", "Intro to Coding",
                               "Learning how to code", "John Doe", "In Person")
        self.assertEqual(self.course.Course_Code, "102", "Expected code 102, got: " + str(self.course.Course_Code))

    def test_edit_name(self):
        Supervisor.edit_course(self.course, "101", "Intermediate Coding",
                               "Learning how to code", "John Doe", "In Person")
        self.assertEqual(self.course.Course_Name, "Intermediate Coding",
                         "Expected name: Intermediate Coding, got: " + str(self.course.Course_Name))

    def test_edit_description(self):
        Supervisor.edit_course(self.course, "101", "Intro to Coding",
                               "Learning more about code", "John Doe", "In Person")
        self.assertEqual(self.course.Course_Description, "Learning more about code",
                         "Expected description: Learning more about code, got: " + str(self.course.Course_Description))

    def test_edit_instructor(self):
        Supervisor.edit_course(self.course, "101", "Intro to Coding",
                               "Learning how to code", "Jane Doe", "In Person")
        self.assertEqual(self.course.Course_Instructor, "Jane Doe",
                         "Expected instructor: Jane Doe, got: " + str(self.course.Course_Instructor))

    def test_edit_instruction_method(self):
        Supervisor.edit_course(self.course, "101", "Intro to Coding",
                               "Learning how to code", "John Doe", "Hybrid")
        self.assertEqual(self.course.Course_Instruction_Method, "Hybrid",
                         "Expected instruction method: Hybrid, got: " + str(self.course.Course_Instruction_Method))
