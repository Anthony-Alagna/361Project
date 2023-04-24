from myapp.models import User, Course
from myapp.Classes.users import Users


class Supervisor(Users):
    @staticmethod
    def create_account(fname, lname, email, username, password, address, city, phone, account_type):
        users = User.objects.all()
        for user in users:
            if user.User_LogName == username:
                return TypeError(
                    "username already exists")

        if fname == "" or lname == "" or email == "" or username == "" or password == "" or address == "" or city == "" or phone == "" or account_type == "":
            return TypeError(
                "missing field")

        else:
            user = User.objects.create(User_fName=fname, User_lName=lname, User_Email=email, User_LogName=username,
                                       User_LogPass=password, User_Address=address, User_City=city, User_Phone=phone,
                                       User_Pos=account_type)
            return user

    def checkInstructorInCourse(instructor_name, course_code):
        if instructor_name == "" or course_code == "":
            return TypeError("instructor name is blank or course id name is blank")
        else:
            course = Course.objects.get(Course_Code=course_code)
            if course is None:
                return TypeError("the course you search does not exist")
            elif course.Course_Instructor is not None:
                return TypeError("you must remove instructor before you can add new one")
            elif course.Course_Instructor == instructor_name:
                return TypeError("course instructor with the name {{instructor_code}} name is already addd")
            else:
                return True

    @staticmethod
    def removeInstructorFromClass(instructor_name, course_code):
        if not Supervisor.checkInstructorInCourse(instructor_name, course_code):
            return TypeError("instructor name is blank or course id name is blank")
        else:
            course = Course.objects.get(Course_Code=course_code)
            course.Course_Instructor = ""
            course.save()
            return course

    @staticmethod
    def addInstructor(instructor_name, course_code):
        if not Supervisor.checkInstructorInCourse(instructor_name, course_code):
            return Supervisor.checkInstructorInCourse(instructor_name, course_code)
        else:
            course = Course.objects.get(Course_Code=course_code)
            course.Course_Instructor=instructor_name
            course.save()
            return course

    @staticmethod
    def editCourse(course_name='default', course_desc='default', isonline='default', location='default',
                   begin='default', updated='default'):
        # what do the form fields come through as if they're empty? assuming it's None
        if course_name == "" or course_desc == "" or isonline == "" or location == "":
            return TypeError(
                "cannot leave a value blank")
        else:
            if course_name != 'default':
                Course.objects.update(Course_Name=course_name)
            if course_desc != 'default':
                Course.objects.update(Course_Description=course_desc)
            if isonline != 'default':
                Course.objects.update(Course_isOnline=isonline)
            if location != 'default':
                Course.objects.update(Course_Location=location)

    def deleteUser(username):
        user = User.objects.filter(User_LogName=username)
        user.delete()



