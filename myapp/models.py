from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def active(self):
        return self.filter(active=True)


class Course(models.Model):
    Course_Code = models.CharField(max_length=3)
    Course_Instructor = models.CharField(max_length=50, blank=True)
    Course_Description = models.CharField(max_length=150, blank=True)
    Course_isOnline = models.BooleanField(default=False)
    Course_Location = models.CharField(max_length=50, blank=True)
    Course_begin = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    Course_Updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(
        "User", through='CourseEnrollment', related_name='enrolled_courses')

    def __str__(self):
        return self.name


class Section(models.Model):
    Sec_Name = models.CharField(max_length=200)
    Sec_Location = models.CharField(max_length=200)
    # foreign key for user, is there only one instructor per section/course?
    Sec_Instructor = models.ForeignKey("User", on_delete=models.CASCADE)
    Sec_Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Sec_isOnline = models.BooleanField(default=False)
    Sec_begin = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    Sec_Updated = models.DateTimeField(
        auto_now=True, blank=True, null=True)


class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True, default="")
    username = models.CharField(max_length=200, unique=True, default="")
    password = models.CharField(max_length=200, blank=True)
    positions_choices = [('SA', 'Supervisor'),
                         ('TA', 'Teaching Assistant'), ('IN', 'Instructor')]
    positions = models.CharField(
        max_length=25, blank=True, choices=positions_choices)
    phone_number = models.CharField(max_length=200, blank=True)
    address = models.TextField(max_length=500, blank=True)
    city = models.CharField(max_length=200, blank=True)
    is_grader = models.BooleanField(default=False)
    courses = models.ManyToManyField(
        "Course", through="CourseEnrollment", related_name="assigned_users", blank=True
    )
    pw_reset_token = models.CharField(
        max_length=40, blank=True, default='')
    sections = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name='enrolled_users')
    created_at = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)


class CourseEnrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_instructor = models.BooleanField(default=False)
    is_TA = models.BooleanField(default=False)
    is_grader = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Course Enrollments"
        unique_together = ("course", "user")
