
# from django.test import TestCase
# from datetime import datetime
#
# from myapp.Classes.supervisor import Supervisor
# from myapp.models import User, Course, Section
#
#
# class SectionTestCase(TestCase):
#     def setUp(self):
#         self.u1 = User.objects.create(id='1', User_first_name="John", User_last_name="Doe", email="john.doe@example.com",
#                                       User_Pos="Supervisor")
#         self.u2 = User.objects.create(id='2', User_first_name="help", User_last_name="us", email="us.doe@example.com",
#                                       User_Pos="Teaching Assistant")
#         self.course = Course.objects.create(Course_Code="CS101", Course_Name="Introduction to Computer Science")
#
#         self.testSec = Section.objects.create(Sec_Name="Section A", Sec_Location="Room 101",
#                                               Sec_Instructor=self.u2, Sec_Course=self.course)
#
#     def test_create_section(self):
#         sec_name = "Section B"
#         course = "CS101"
#         ta_instr = "2"
#         date_time = datetime.now()
#         created_section = Supervisor.create_section(sec_name=sec_name, course=course, ta_instr=ta_instr,
#                                                     date_time=date_time)
#         check = Section.objects.filter(Sec_Name=created_section.Sec_Name).exists()
#         self.assertTrue(check)
#
#     def test_create_with_blank_section_name(self):
#         sec_name = ""
#         course = "CS101"
#         ta_instr = "2"
#         date_time = datetime.now()
#         with self.assertRaises(ValueError):
#             Supervisor.create_section(sec_name, course, ta_instr, date_time)
#
#     def test_create_with_blank_course(self):
#         sec_name = "Section C"
#         course = ""
#         ta_instr = "2"
#         date_time = datetime.now()
#         with self.assertRaises(ValueError):
#             Supervisor.create_section(sec_name, course, ta_instr, date_time)
#
#     def test_existing_section(self):
#         sec_name = "Section A"
#         course = "CS101"
#         ta_instr = "2"
#         date_time = datetime.now()
#         with self.assertRaises(ValueError):
#             Supervisor.create_section(sec_name, course, ta_instr, date_time)
#
#     def test_delete_section(self):
#         Supervisor.delete_section(self.testSec)
#         result = Section.objects.filter(Sec_Name="Section A").exists()
#         self.assertFalse(result)
