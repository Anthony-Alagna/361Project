from django.db import models
from datetime import datetime



# this is just the start
# we have to redesign this I just started the models class so we can redesign what needs ot be done


class User(models.Model):
    id = models.AutoField(("user_id"), primary_key=True,
                          unique=True)
    User_Name = models.CharField(max_length=200, blank=True)
    User_Email = models.CharField(max_length=200, blank=True)
    User_Type = models.CharField(max_length=200, blank=True)
    User_Phone = models.CharField(max_length=200, blank=True)
    User_Address = models.TextField(max_length=500, blank= True)
    User_LogName = models.CharField(max_length=200, blank=True)
    User_LogPass = models.CharField(max_length=200, blank=True)
    User_isGrader = models.BooleanField(default=False)
    User_SecAssigned = models.ManyToManyField(
        'Course', through='CourseToUser', related_name='users')

    # need courses foreign key

    User_begin = models.DateTimeField(auto_now_add=True)
    User_Updated = models.DateTimeField(auto_now=True)


class Course(models.Model):
    # how do we get the different views for each user?
    id = models.AutoField(("course_id"), primary_key=True,
                          unique=True)
    Course_Name = models.CharField(max_length=50, blank=True)
    Course_Code = models.CharField(max_length=50)
    #each course requires one instructor
    Course_Instructor = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    Course_isOnline = models.BooleanField(default=False)
    Course_Location = models.CharField(max_length=50)
    Course_begin = models.DateTimeField(
        auto_now_add=True)
    Course_Updated = models.DateTimeField(auto_now=True)
    Course_start = models.DateTimeField("start")
    Course_end = models.DateTimeField("end", help_text="The end time must be later than the start time.")


class Section(models.Model):
    id = models.AutoField(("section_id"), primary_key=True,
                          unique=True)
    Sec_Name = models.CharField(max_length=200)
    Sec_Location = models.CharField(max_length=200)
    Sec_Instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    Sec_Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Sec_begin = models.DateTimeField(auto_now_add=True)
    Sec_Updated = models.DateTimeField(auto_now=True)


# this represents many to many
# there is also an instance called ManyToMany in django
class CourseToUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    #printable so we can see what going on
    def __str__(self):
        return self.user.User_Email+ " " + self.course.id
