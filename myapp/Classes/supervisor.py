from myapp.models import User, Course
from myapp.Classes.users import Users


class Supervisor(Users):
    @staticmethod
    def create_account(fname, lname, email, username, password, address, city, phone, account_type):
        users = User.objects.all()
        for user in users:
            if user.User_LogName == username:
                return ValueError(
                    "That username already exists - please choose another")

        if fname == "" or lname == "" or email == "" or username == "" or password == "" or address == "" or city == "" or phone == "" or account_type == "":
            return ValueError(
                "You're missing a field - please fill in all fields")

        else:
            user = User.objects.create(User_fName=fname, User_lName=lname, User_Email=email, User_LogName=username,
                                       User_LogPass=password, User_Address=address, User_City=city, User_Phone=phone,
                                       User_Pos=account_type)
            return user

    @staticmethod
    def create_course(code, name, desc, inst):
        courses = Course.objects.all()
        for course in courses:
            if course.Course_Code == code:
                return TypeError("A course with that code already exists!")
        if code == "":
            return TypeError("Course code cannot be blank!")
        elif name == "":
            return TypeError("Course name cannot be blank!")
        elif desc == "":
            return TypeError("Course description cannot be blank!")
        return Course.objects.create(Course_Code=code, Course_Name=name, Course_Description=desc,
                                     Course_Instructor=inst)

    def checkInstructorInCourse(instructor_name, course_code):
        if instructor_name == "" or course_code == "":
            return TypeError("instructor name is blank or course id name is blank")
        else:
            course = Course.objects.get(Course_Code=course_code)
            if course is None:
                return TypeError("the course you search does not exist")
            elif course.Course_Instructor is not None:
                return TypeError("you must remove instructor before you can add new one")
            else:
                return True

    @staticmethod
    def removeInstructorFromClass(instructor_name, course_code):
        if not Supervisor.checkInstructorInCourse(instructor_name, course_code):
            return ValueError("instructor name is blank or course id name is blank")
        else:
            course = Course.objects.get(Course_Code=course_code)
            course.Course_Instructor = ""
            course.save()
            return course

    @staticmethod
    def addInstructor(ins_fname, ins_lname, course_code):
        #checks if user is real
        if ins_fname == "" or ins_lname == "":
            return ValueError("cannot figure out user if first name or last name are inputted as a blank")
        user_f = User.objects.get(User_fName=ins_fname)
        user_l = User.objects.get(User_lName=ins_lname)

        if user_f.User_fName == user_l.User_fName and user_f.User_lName == user_l.User_lName:
            if not Supervisor.checkInstructorInCourse(user_f, course_code):
                return Supervisor.checkInstructorInCourse(user_f, course_code)
            else:
                course = Course.objects.get(Course_Code=course_code)
                course.Course_Instructor = user_f.User_fName
                course.save()
                return course
        else:
            return ValueError("user with this first and last name does not exist")

    @staticmethod
    def editCourse(course_name=Course.Course_Name, course_desc=Course.Course_Description,
                   isonline=Course.Course_isOnline, location=Course.Course_Location,
                   begin='default', updated='default'):
        # what do the form fields come through as if they're empty? assuming it's None
        if course_name == "" or course_desc == "" or isonline == "" or location == "":
            return ValueError(
                "cannot make a value blank")
        else:
            if course_name != Course.Course_Name:
                Course.objects.update(Course_Name=course_name)
            if course_desc != Course.Course_Description:
                Course.objects.update(Course_Description=course_desc)
            if isonline != Course.Course_isOnline:
                Course.objects.update(Course_isOnline=isonline)
            if location != Course.Course_Location:
                Course.objects.update(Course_Location=location)

    def deleteUser(username):
        user = User.objects.filter(User_LogName=username)
        user.delete()
