from django.test import TestCase, Client
from myapp.models import User, Course


# M: As a supervisor I would like to assign instructors to courses so that they are able to manage their course


class TestInstructorsInCourse(TestCase):
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
        self.course2 = Course.objects.create(Course_ID='2', Course_Name='Computer Architecture', Course_Code='482-01',
                                             Course_Instructor=self.user2, Course_isOnline='False',
                                             Course_Location='123 Main St',
                                             User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')
        self.course3 = Course.objects.create(
            Course_ID='3', Course_Name='Python for Beginners', Course_Code='101-01',
            Course_Instructor="", Course_isOnline='True',
            Course_Location='Online',
            User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00'
        )

    def test_user_teaches_course(self):
        testIns = Course.objects.get(Course_ID='c1')
        instructor = User.getInstructor(self.course1)
        self.assertEqual(testIns.Course_Instructor, instructor,
                         "instructor is properly located by the getInstructor function")


# test the instructor  a class with no instructor, and instructor with
# test location when isOnline
class AddInstructorsToCourse(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(id='1', User_Name='Cricket', User_Email='user1@example.com',
                                         User_Type='instructor', User_Phone='1234567890', User_Address='123 Main St',
                                         User_LogName='user1', User_LogPass='password', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')
        self.user2 = User.objects.create(id='2', User_Name='taco', User_Email='user2@example.com',
                                         User_Type='insturctor', User_Phone='0987654321', User_Address='456 Elm St',
                                         User_LogName='user2', User_LogPass='password2', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-17 00:00:00')
        self.user3 = User.objects.create(id='3', User_Name='Noodle', User_Email='user3@example.com',
                                         User_Type='TA', User_Phone='034567921', User_Address='22 blanco Dr',
                                         User_LogName='user2', User_LogPass='password3', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-17 00:00:00')
        self.course1 = Course.objects.create(Course_ID='c1', Course_Name='Lion King analysis', Course_Code='382-01',
                                             Course_Instructor=self.user1, Course_isOnline='False',
                                             Course_Location='123 Main St',
                                             User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')
        self.course2 = Course.objects.create(Course_ID='c2', Course_Name='Computer Architecture', Course_Code='482-01',
                                             Course_Instructor=self.user2, Course_isOnline='False',
                                             Course_Location='123 Main St',
                                             User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')
        self.course3 = Course.objects.create(
            Course_ID='c3', Course_Name='Python for Beginners', Course_Code='101-01',
            Course_Instructor="", Course_isOnline='True',
            Course_Location='Online',
            User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00'
        )

    def test_add_teacher_to_class_with_no_instructor(self):
        teacher = self.user1
        User.assignInstructors(self.course3.Course_Code, self.user1)
        course = Course.objects.get(Course_ID='c2')
        self.assertIn(teacher, course.Course_Instructor, "teacher should be added because it was blank")

    def test_add_ta_to_instructor_position(self):
        User.assignInstructors(self.course3.Course_Code, self.id())
        course = Course.objects.get(Course_ID='c3')
        self.assertEqual("", course.Course_Instructor,
                         "teacher should be added because a TA was inapporpriatly added to the Instructor position")

    def test_add_blank_user_to_course(self):
        User.assignInstructors(self.course3.Course_Code, "")
        course = Course.objects.get(Course_ID='c3')
        self.assertEqual("", course.Course_Instructor,
                         "cannot add a blank instructor to course")

    def test_add_multiple_instructors(self):
        User.assignInstructors(self.course3.Course_Code, self.user2.id)
        course = Course.objects.get(Course_ID='c2')
        self.assertEqual('1', course.objects.filter(Course_ID='2').count(),
                         "there should only be on isntructor that can be assigned toa  course")

    def test_remove_instructor(self):
        User.removeInstructor(self.course2.Course_Code, self.user2.id)
        course = Course.objects.get(Course_ID='c2')
        self.assertEqual(0, course.objects.filter(Course_ID='2').count(),
                         "there should only be on isntructor that can be assigned toa  course")

    def test_remove_blank_instructor(self):
        course = Course.objects.get(Course_ID='c3')
        init_length = len(course.Course_Instructor)
        User.removeInstructor(self.course3.Course_Code, self.course3.id)

        self.assertEqual(init_length, len(course.Course_Instructor), "nothing to remove already blank")

    def test_replace_instructor(self):
        course1 = Course.objects.get(Course_ID='c1')
        course2 = Course.objects.get(Course_ID='c2')
        inst1 = course1.Course_Instructor
        inst2 = course2.Course_Instructor
        User.removeInstructor(self.course3.Course_Code, self.course2.id)
        User.removeInstructor(self.course3.Course_Code, self.course1.id)
        self.assertEqual(inst1, course2.Course_Instructor,
                         "the course 1 instructor should not have been added to course 2")
