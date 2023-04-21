from django.test import TestCase, Client
from myapp.models import User, Course
from myapp.views import CreateCourse


# M: As a supervisor I want to be able to create courses, so that I can assign instructors and TAs to courses.


class TestNewCourse(TestCase):
    supervisor = None
    def setUp(self):
        self.supervisor = Client()
        self.user1 = User.objects.create(
            id='1', User_Name='John Doe', User_Email='user1@example.com',
            User_Type='instructor', User_Phone='1234567890', User_Address='123 Main St',
            User_LogName='user1', User_LogPass='password', User_isGrader='no',
            User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')

        self.course1 = Course.objects.create(
            Course_ID='1', Course_Name='Lion King analysis', Course_Code='382-01',
            Course_Instructor=self.user1, Course_isOnline='False',
            Course_Location='123 Main St',
            User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')
    def test_course_name(self):
        Course.
