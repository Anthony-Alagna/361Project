from django.db import models


# we have to redesign this I just started the models class so we can redesign what needs ot be done
class User(models.Model):
    User_ID = models.CharField(max_Length=200)
    User_Name = models.CharField(max_Length=200)
    User_Email = models.CharField(max_length=200)
    User_Type = models.CharField(max_length=200)
    User_Phone = models.CharField(max_length=200)
    User_Address = models.TextField(max_length=500)
    User_LogName = models.CharField(max_length=200)
    User_LogPass = models.CharField(max_length=200)
    User_isGrader = models.CharField(max_length=3)
    User_SecAssigned = models.ManyToManyField('Course', through='Course', related_name='users')
    # need courses foreign key

    User_begin = models.DateTimeField("date published")
    User_Updated = models.DateTimeField("date published")


class Course(models.Model):
    # how do we get the different views for each user?
    Course_ID = models.CharField(max_Length=50)
    Course_Name = models.CharField(max_Length=50)
    Course_Code = models.CharField(max_Length=50)
    Course_Instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    Course_isOnline = models.CharField(max_Length=6)
    Course_Location = models.CharField(max_Length=50)
    Course_begin = models.DateTimeField("date published")
    Course_Updated = models.DateTimeField("date published")


class Section(models.Model):
    Sec_ID = models.CharField(max_Length=200)

    Sec_Name = models.CharField(max_Length=200)
    Sec_Location = models.CharField(max_Length=200)
    # foreign key for user, is there only one instructor per section/course?
    Sec_Instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    Sec_Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Sec_isOnline = models.CharField(max_length=7)
    Sec_begin = models.DateTimeField("date published")
    Sec_Updated = models.DateTimeField("date published")


# this represents many to many
# there is also an instance called ManyToMany in django
class courseToUser(models.Model):
    id = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course = models.ForeignKey(Section, on_delete=models.CASCADE)
