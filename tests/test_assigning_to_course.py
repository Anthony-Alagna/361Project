
from django.test import TestCase, Client
from myapp.models import User, Course


# M: As a supervisor I would like to assign instructors to courses so that they are able to manage their course


class TestSearchCourse(TestCase):
    def setup(self):
        self.user1 = User.objects.create(id='1', User_Name='Cricket', User_Email='user1@example.com',
                                         User_Type='TA', User_Phone='1234567890', User_Address='123 Main St',
                                         User_LogName='user1', User_LogPass='password', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')
        self.user2 = User.objects.create(id='2', User_Name='Noodle', User_Email='user2@example.com',
                                         User_Type='TA', User_Phone='0987654321', User_Address='456 Elm St',
                                         User_LogName='user2', User_LogPass='password1', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-17 00:00:00')
        self.course1 = Course.objects.create(Course_ID='1', Course_Name='Lion King analysis', Course_Code='382-01',
                                             Course_Instructor=self.user1, Course_isOnline='False',
                                             Course_Location='123 Main St',
                                             User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')
        self.course1 = Course.objects.create(Course_ID='2', Course_Name='Computer ', Course_Code='482-01',
                                             Course_Instructor=self.user1, Course_isOnline='False',
                                             Course_Location='123 Main St',
                                             User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')
        self.course3 = Course.objects.create(
            Course_ID='3', Course_Name='Python for Beginners', Course_Code='101-01',
            Course_Instructor=self.user2, Course_isOnline='True',
            Course_Location='Online',
            User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00'
        )

    def test_search_existing_course(self):
        course_name = "Lion King analysis"
        result = User.searchCourse(course_name)
        self.assertEqual(result, self.course1.Course_Name)
    def test_course_name_with_incorrect_typing(self):
        course_name = "Lion King analysis"
        result = User.searchCourse(course_name)
        self.assertEqual(result, self.course1.Course_Name)



class TestInstructorsinCourses(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(id='1', User_Name='Cricket', User_Email='user1@example.com',
                                         User_Type='TA', User_Phone='1234567890', User_Address='123 Main St',
                                         User_LogName='user1', User_LogPass='password', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')
        self.user2 = User.objects.create(id='2', User_Name='Noodle', User_Email='user2@example.com',
                                         User_Type='TA', User_Phone='0987654321', User_Address='456 Elm St',
                                         User_LogName='user2', User_LogPass='password1', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-17 00:00:00')
        self.course1 = Course.objects.create(Course_ID='1', Course_Name='Lion King analysis', Course_Code='382-01',
                                             Course_Instructor=self.user1, Course_isOnline='False',
                                             Course_Location='123 Main St',
                                             User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')
        self.course1 = Course.objects.create(Course_ID='2', Course_Name='Computer ', Course_Code='482-01',
                                             Course_Instructor=self.user1, Course_isOnline='False',
                                             Course_Location='123 Main St',
                                             User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')
        self.course3 = Course.objects.create(
            Course_ID='3', Course_Name='Python for Beginners', Course_Code='101-01',
            Course_Instructor=self.user2, Course_isOnline='True',
            Course_Location='Online',
            User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00'
        )
    def test_user_teaches_course(self):
        teacher= "user1"
        instructor = Course.getInstructor(self.course1)
        self.assertEqual(teacher, instructor)
    def test_user_teaches_course(self):
        teacher= "user1"
        instructor = Course.getInstructor(self.course1)
        self.assertEqual(teacher, instructor)










# test the instructor  a class with no instructor, and instructor with
# test location when isOnline


class TestAssignUser(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(id='1', User_Name='Cricket', User_Email='user1@example.com',
                                         User_Type='TA', User_Phone='1234567890', User_Address='123 Main St',
                                         User_LogName='user1', User_LogPass='password', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')
        self.user2 = User.objects.create(id='2', User_Name='Noodle', User_Email='user2@example.com',
                                         User_Type='TA', User_Phone='0987654321', User_Address='456 Elm St',
                                         User_LogName='user2', User_LogPass='password1', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-17 00:00:00')

