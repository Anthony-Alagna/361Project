from django.db import models
from datetime import datetime


# this is just the start
# we have to redesign this I just started the models class so we can redesign what needs ot be done


class User(models.Model):
    id = models.AutoField(("user_id"), primary_key=True,
                          unique=True, default=0)
    User_Name = models.CharField(max_length=200)
    User_Email = models.CharField(max_length=200)
    User_Type = models.CharField(max_length=200)
    User_Phone = models.CharField(max_length=200)
    User_Address = models.TextField(max_length=500)
    User_LogName = models.CharField(max_length=200)
    User_LogPass = models.CharField(max_length=200)
    User_isGrader = models.CharField(max_length=3)
    User_SecAssigned = models.ManyToManyField(
        'Course', through='CourseToUser', related_name='users')

    # need courses foreign key

    User_begin = models.DateTimeField(auto_now_add=True)
    User_Updated = models.DateTimeField(auto_now=True)


class Course(models.Model):
    # how do we get the different views for each user?
    id = models.AutoField(("course_id"), primary_key=True,
                          unique=True, default=0)
    Course_Name = models.CharField(max_length=50)
    Course_Code = models.CharField(max_length=50)
    Course_Instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    Course_isOnline = models.CharField(max_length=6)
    Course_Location = models.CharField(max_length=50)
    Course_begin = models.DateTimeField(
        auto_now_add=True)
    Course_Updated = models.DateTimeField(auto_now=True)


class Section(models.Model):
    id = models.AutoField(("section_id"), primary_key=True,
                          unique=True, default=0)
    Sec_Name = models.CharField(max_length=200)
    Sec_Location = models.CharField(max_length=200)
    # foreign key for user, is there only one instructor per section/course?
    Sec_Instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    Sec_Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Sec_isOnline = models.CharField(max_length=7)
    Sec_begin = models.DateTimeField(auto_now_add=True)
    Sec_Updated = models.DateTimeField(auto_now=True)


# this represents many to many
# there is also an instance called ManyToMany in django
class CourseToUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
