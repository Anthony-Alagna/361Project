import unittest
from django.test import TestCase
from datetime import datetime

from myapp.Classes.supervisor import Supervisor
from myapp.models import User, Course, Section


class SectionTestCase(TestCase):
    def setUp(self):
        self.u1 = User.objects.create(User_fName="John", User_lName="Doe", email="john.doe@example.com",
                                      User_Pos="Supervisor")
        self.u2 = User.objects.create(User_fName="help", User_lName="us", email="us.doe@example.com",
                                      User_Pos="Teaching Assistant")
        self.course = Course.objects.create(Course_Code="CS101", Course_Name="Introduction to Computer Science")

        self.testSec = Section.objects.create(Sec_Name="Section A", Sec_Location="Room 101",
                                              Sec_Instructor=self.u2, Sec_Course=self.course)

    def test_create_section(self):
        sec_name = "Section B"
        course = self.course
        ta_instr = self.u2
        date_time = datetime.now()
        created_section = Supervisor.create_section(sec_name="section b", course=course, ta_instr=ta_instr,
                                                    date_time=date_time)
        check = Section.objects.filter(Sec_Name=created_section.Sec_Name).exists()
        self.assertTrue(check)

    def test_create_with_blank_section_name(self):
        sec_name = ""
        course = self.course
        ta_instr = self.u2
        date_time = datetime.now()
        result = Supervisor.create_section("", course, ta_instr, date_time)
        self.assertTrue(
            isinstance(result, TypeError), "Expected a type error from create_course"
        )

    def test_create_with_blank_course(self):
        sec_name = ""
        course = self.course
        ta_instr = self.u2
        date_time = datetime.now()
        result = Supervisor.create_section("Section c", "", ta_instr, date_time)
        self.assertTrue(
            isinstance(result, TypeError), "Expected a type error from create_course"
        )

    def test_extisting_section(self):
        sec_name = ""
        course = self.course
        ta_instr = self.u2
        date_time = datetime.now()
        result = Supervisor.create_section("Section A", "", ta_instr, date_time)
        self.assertTrue(
            isinstance(result, TypeError), "Expected a type error from create_course as the section exists"
        )

    def test_delete_section(self):
        Supervisor.delete_section(self.testSec)
        result = Section.objects.filter(Sec_Name="Section A").exists()
        self.assertFalse(result)