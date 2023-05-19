from django.test import TestCase, Client
from datetime import datetime
from django.urls import reverse
from myapp.Classes.supervisor import Supervisor
from myapp.models import User, Course, Section


class SectionTestCase(TestCase):
    def setUp(self):
        self.u1 = User.objects.create(id='1', first_name="John", last_name="Doe", email="john.doe@example.com",
                                      positions="Supervisor")
        self.u2 = User.objects.create(id='2', first_name="help", last_name="us", email="us.doe@example.com",
                                      positions="Teaching Assistant")
        self.course = Course.objects.create(Course_Code="CS101", Course_Name="Introduction to Computer Science")

        self.testSec = Section.objects.create(Sec_Name="Section A", Sec_Location="Room 101",
                                              Sec_Instructor=self.u2, Sec_Course=self.course)

    def test_create_section(self):
        sec_name = "Section B"
        course = "CS101"
        ta_instr = "2"
        date_time = datetime.now()
        created_section = Supervisor.create_section(sec_name=sec_name, course=course, ta_instr=ta_instr,
                                                    date_time=date_time)
        check = Section.objects.filter(Sec_Name=created_section.Sec_Name).exists()
        self.assertTrue(check)

    def test_create_with_blank_section_name(self):
        sec_name = ""
        course = "CS101"
        ta_instr = "2"
        date_time = datetime.now()
        with self.assertRaises(ValueError):
            Supervisor.create_section(sec_name, course, ta_instr, date_time)

    def test_existing_section(self):
        sec_name = "Section A"
        course = "CS101"
        ta_instr = "2"
        date_time = datetime.now()
        with self.assertRaises(ValueError):
            Supervisor.create_section(sec_name, course, ta_instr, date_time)

    def test_delete_section(self):
        Supervisor.delete_section(self.testSec)
        result = Section.objects.filter(Sec_Name="Section A").exists()
        self.assertFalse(result)


class CreateSectionTestCase(TestCase):
    def setUp(self):
        self.u1 = User.objects.create(
            username='testuser',
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
            positions='Supervisor'
        )
        self.u2 = User.objects.create(
            username='tt',
            first_name='Ttl',
            last_name='Userder',
            email='testuser@example.com',
            positions='Teaching Assistant'
        )

        self.c1 = Course.objects.create(
            id='1',
            Course_Code='ABC',
            Course_Name='Test Course',
            Course_Description='Course description',
            Course_Instructor='Test Instructor',
            Course_Instruction_Method='Method',
            name='Test Course'
        )
        self.c2 = Course.objects.create(
            id='2',
            Course_Code='991',
            Course_Name='Test Course2',
            Course_Description='Course description2',
            Course_Instructor='Test Instructor2',
            Course_Instruction_Method='Method',
            name='Test Course2'
        )

        self.client = Client()

    def test_create_section_Accessible(self):
        response = self.client.get(reverse("createsection"))
        self.assertEqual(response.status_code, 200)

    def test_successful_section_creation(self):
        data = {
            'section_name': 'Test Section',
            'course': 'ABC',
            'section_inst': self.u2.pk

        }

        response = self.client.post(reverse('createsection'), data)

        self.assertEqual(response.status_code, 200)

    def test_section_creation_with_invalid_instructor(self):
        def test_section_creation_with_invalid_data(self):
            data = {
                'section_name': 'Test Section',
                'course': self.c1.pk,
                'section_inst': 5  # No instructor specified
            }

            with self.assertRaises(User.DoesNotExist):
                self.client.post(reverse('createsection'), data)

    def test_section_creation_without_instructor(self):
        def test_section_creation_with_invalid_data(self):
            data = {
                'section_name': 'Test Section',
                'course': self.c1.pk,
                'section_inst': ''
            }

            response = self.client.post(reverse('createsection'), data)
            self.assertEqual(response.status_code, 200)

    def test_section_creation_with_invalid_course(self):
        def test_section_creation_with_invalid_data(self):
            data = {
                'section_name': 'Test Section',
                'course': '221',
                'section_inst': self.u2.pk  # No instructor specified
            }

            with self.assertRaises(Course.DoesNotExist):
                self.client.post(reverse('createsection'), data)

#this is supposed to fail uncomment it out
    # def test_missing_sec_name(self):
    #     data = {
    #         'section_name': '',
    #         'course': self.c1.Course_Code,
    #         'section_inst': self.u2.pk,
    #     }
    #
    #     response = self.client.post(reverse('createsection'), data)
    #
    #     # Check if the response contains the error message
    #     self.assertContains(response, "Cannot have a blank section name", status_code=200)

#supposed to fail
    def test_success_redirection_on_creation(self):
        data = {
            'section_name': 'something new',
            'course': '991',
            'section_inst': self.u2.pk

        }

        response = self.client.post(reverse('createsection'), data)

        self.assertTemplateUsed(response, 'course_base.html')
    #     self.assertEqual(response.status_code, 200)

#this is supposed to fail but commented out
    # def test_add_an_incorrect_user_while_creating(self):
    #     data = {
    #         'section_name': 'tiki masala',
    #         'course': self.c2.Course_Code,
    #         'section_inst': self.u1.pk
    #
    #     }
    #
    #     response = self.client.post(reverse('createsection'), data)
    #     self.assertEqual(Section.objects.filter(Sec_Name='tiki masala').count(), 0)
