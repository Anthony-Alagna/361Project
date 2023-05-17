# from django.test import TestCase, Client
from myapp.models import User, Course
from myapp.Classes.supervisor import Supervisor
from django.test import TestCase, Client
from django.urls import reverse


#
#
#  M: As a supervisor I would like to assign instructors to courses so that they are able to manage their course
#
#

#  M: As a supervisor I would like to assign instructors to courses so that they are able to manage their course
#
#


# test the instructor  a class with no instructor, and instructor with
# test location when isOnline
# class AddInstructorsToCourse(TestCase):
#     def setUp(self):
#         self.user1 = User.objects.create(
#             id="1",
#             User_fName="Cricket",
#             User_lName="ROCKET",
#             email="user1@example.com",
#             User_Pos="instructor",
#             User_Phone="1234567890",
#             User_Address="123 Main St",
#             User_LogPass="password",
#             User_isGrader="True",
#             User_begin="2022-01-01 00:00:00",
#             User_Updated="2023-04-18 00:00:00",
#         )
#         self.user2 = User.objects.create(
#             id="2",
#             User_fName="taco",
#             User_lName="roco",
#             email="user2@example.com",
#             User_Pos="insturctor",
#             User_Phone="0987654321",
#             User_Address="456 Elm St",
#             User_LogPass="password2",
#             User_isGrader="True",
#             User_begin="2022-01-01 00:00:00",
#             User_Updated="2023-04-17 00:00:00",
#         )
#         self.user3 = User.objects.create(
#             id="3",
#             User_fName="Noodle",
#             User_lName="String",
#             email="user3@example.com",
#             User_Pos="Teaching Assistant",
#             User_Phone="034567921",
#             User_Address="22 blanco Dr",
#             User_LogPass="password3",
#             User_isGrader="False",
#             User_begin="2022-01-01 00:00:00",
#             User_Updated="2023-04-17 00:00:00",
#         )
#         self.course1 = Course.objects.create(
#             id="1",
#             Course_Name="Lion King analysis",
#             Course_Code="382-01",
#             Course_Instructor=self.user1,
#             Course_isOnline="False",
#             Course_Location="123 Main St",
#             Course_begin="2022-01-01 00:00:00",
#             Course_Updated="2023-04-18 00:00:00",
#         )
#         self.course2 = Course.objects.create(
#             id="2",
#             Course_Name="Computer Architecture",
#             Course_Code="48201",
#             Course_Instructor=self.user2.User_fName,
#             Course_isOnline="False",
#             Course_Location="123 Main St",
#             Course_begin="2022-01-01 00:00:00",
#             Course_Updated="2023-04-18 00:00:00",
#         )
#         self.course3 = Course.objects.create(
#             id="3",
#             Course_Name="Python for Beginners",
#             Course_Code="10101",
#             Course_Instructor="",
#             Course_isOnline="True",
#             Course_Location="Online",
#             Course_begin="2022-01-01 00:00:00",
#             Course_Updated="2023-04-18 00:00:00",
#         )
#
#     # check that you can add to course with no instructor in it
#     def test_add_teacher_to_class_with_no_instructor(self):
#         teacher = self.user1
#         Supervisor.addInstructor(
#             self.user1.User_fName, self.course3.Course_Code)
#         course = Course.objects.get(id="3")
#         self.assertEqual(
#             teacher.User_fName,
#             course.Course_Instructor,
#             "teacher should be added because it was blank",
#         )
#
#     # test removing a professor from course
#     def test_removing_teacher_from_course(self):
#         course = Course.objects.get(id="3")
#         Supervisor.removeInstructorFromClass(
#             course.Course_Instructor, course_code=course.Course_Code
#         )
#         self.assertEqual(
#             "", course.Course_Instructor, "teacher should be added because it was blank"
#         )
#
#     # test adding a user who is a TA to the instructor pos
#     def test_add_ta_to_instructor_position(self):
#         course = Course.objects.get(id="3")
#         Supervisor.removeInstructorFromClass(
#             course.Course_Instructor, course_code=course.Course_Code
#         )
#         Supervisor.addInstructor(
#             self.user3.User_fName, self.course3.Course_Code)
#
#         self.assertEqual(
#             "",
#             course.Course_Instructor,
#             "teacher should be added because a TA was inapporpriatly added to the Instructor position",
#         )
#
#     # adding a blank user to course
#     def test_add_blank_user_to_course(self):
#         course = Course.objects.get(id="3")
#
#         course = Supervisor.removeInstructorFromClass(
#             course.Course_Instructor, course_code=course.Course_Code
#         )
#         Supervisor.addInstructor("", self.course3.Course_Code)
#
#         self.assertEqual(
#             "", course.Course_Instructor, "can add a blank instructor to course"
#         )
#         # checking the method checks for blank user input
#
#     def test_add_blank_user_to_course_valcheck(self):
#         course = Course.objects.get(id="3")
#         res = Supervisor.removeInstructorFromClass(
#             course.Course_Instructor, course_code=course.Course_Code
#         )
#         res = Supervisor.addInstructor("", self.course3.Course_Code)
#         self.assertEqual(
#             course.Course_Instructor, "", "can add a blank instructor to course"
#         )
#
#     # tests that only one instructor can be added at a time
#     def test_add_multiple_instructors(self):
#         Supervisor.addInstructor(
#             self.user2.User_fName, self.course3.Course_Code)
#         course = Course.objects.get(id="2")
#         self.assertEqual(
#             1,
#             Course.objects.filter(id="2")
#             .values("Course_Instructor")
#             .distinct()
#             .count(),
#             "there should only be one instructor that can be assigned to a course",
#         )
#
#     # removing instructor
#     def test_remove_instructor(self):
#         course = Course.objects.get(id="2")
#         user = User.objects.get(User_fName=course.Course_Instructor)
#         Supervisor.removeInstructorFromClass(
#             course.Course_Instructor, course_code=course.Course_Code
#         )
#         course = Course.objects.get(id="2")
#         self.assertEqual(
#             "",
#             course.Course_Instructor,
#             "there should only be on isntructor that can be assigned toa  course",
#         )
#
#     # tests removing blank instructor
#     def test_remove_blank_instructor(self):
#         course = Course.objects.get(id="3")
#         Supervisor.addInstructor(
#             self.user2.User_fName, self.course3.Course_Code)
#         rest1 = Supervisor.removeInstructorFromClass(
#             self.course3.Course_Instructor, self.course3.Course_Code
#         )
#         res = Supervisor.removeInstructorFromClass(
#             self.course3.Course_Instructor, self.course3.Course_Code
#         )
#         self.assertEqual(
#             res.Course_Instructor, "", "nothing to remove since it is blank"
#         )
#
#
# class TestFunction(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.course3 = Course.objects.create(
#             id="3",
#             Course_Name="Python for Beginners",
#             Course_Code="10101",
#             Course_Instructor="",
#             Course_Instruction_Method="True",
#         )
#         self.user1 = User.objects.create(
#             id="1",
#             User_fName="Cricket",
#             User_lName="ROCKET",
#             email="user1@example.com",
#             User_Pos="instructor",
#             User_Phone="1234567890",
#             User_Address="123 Main St",
#             User_LogPass="password",
#             User_isGrader="True",
#             User_begin="2022-01-01 00:00:00",
#             User_Updated="2023-04-18 00:00:00",
#         )
#         self.user2 = User.objects.create(
#             id="2",
#             User_fName="taco",
#             User_lName="roco",
#             email="user2@example.com",
#             User_Pos="insturctor",
#             User_Phone="0987654321",
#             User_Address="456 Elm St",
#             User_LogPass="password2",
#             User_isGrader="True",
#             User_begin="2022-01-01 00:00:00",
#             User_Updated="2023-04-17 00:00:00",
#         )
#
#     # click on edit button from course_base page
#     def test_go_course_edit_from_base(self):
#         ext = self.course3.Course_Code
#         url = reverse("courseedit", kwargs={"Course_Code": ext})
#         res = self.client.get(url)
#         self.assertEqual(res.status_code, 200)
#
#     # save button click when successful
#
#     # tests what happens after a post to the courseedit page
#     def test_edit_success_on_save(self):
#         ext = self.course3.Course_Code
#
#         # since i added variable to end of url this is how I have to test the url in reverse
#         url = reverse("courseedit", kwargs={"Course_Code": ext})
#
#         response = self.client.post(
#             url, data={"course_inst": self.user2.User_fName,
#                        "save_ch": "submit"}
#         )
#         self.assertEqual(response.status_code, 200)
#
#     # test redirect on unsuccessful post to the same page
#     def test_blank_edit_fail_on_save(self):
#         ext = Course.objects.get(id="3")
#         reversed_url = reverse("courseedit", args=[ext.Course_Code])
#         expected_url = "/home/course_base/courseedit/10101"
#         assert reversed_url == expected_url
#
#     def test_blank_correct_user_fail_on_save(self):
#         ext = Course.objects.get(id="3")
#         url = reverse("courseedit", kwargs={"Course_Code": ext.Course_Code})
#         res = self.client.post(
#             url, data={"course_inst": self.user2.User_fName,
#                        "save_ch": "submit"}
#         )
#         # Check if the response is a redirect
#         self.assertEqual(res.status_code, 200)
