from myapp.models import User, Course
from myapp.Classes.users import Users


class Supervisor(Users):
    @staticmethod
    def create_account(
            fname, lname, email, username, password, address, city, phone, account_type
    ):
        users = User.objects.all()
        for user in users:
            if user.User_LogName == username:
                return ValueError(
                    "That username already exists - please choose another"
                )

        if (
                fname == ""
                or lname == ""
                or email == ""
                or username == ""
                or password == ""
                or address == ""
                or city == ""
                or phone == ""
                or account_type == ""
        ):
            return ValueError("You're missing a field - please fill in all fields")

        else:
            user = User.objects.create(
                User_fName=fname,
                User_lName=lname,
                User_Email=email,
                User_LogName=username,
                User_LogPass=password,
                User_Address=address,
                User_City=city,
                User_Phone=phone,
                User_Pos=account_type,
            )
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
        return Course.objects.create(
            Course_Code=code,
            Course_Name=name,
            Course_Description=desc,
            Course_Instructor=inst,
        )

    @staticmethod
    def removeInstructorFromClass(instructor_name, course_code):
        if course_code == "":
            return ValueError("course id name is blank")
        else:
            course = Course.objects.get(Course_Code=course_code)
            course.Course_Instructor = ""
            course.save()
            return course

    @staticmethod
    def addInstructor(ins_fname, course_code):
        # checks if user is real
        if course_code == "":
            return ValueError(
                "Cannot eddit course instructor because course code was blank"
            )

        course = Course.objects.get(Course_Code=course_code)
        cTeacher = course.Course_Instructor

        if course.Course_Instructor == ins_fname:
            return ValueError("professor already assigned to this course")

        else:

            course.Course_Instructor = ins_fname
            course.save()
            return course

    @staticmethod
    def editCourse(
            course_name=Course.Course_Name,
            course_desc=Course.Course_Description,
            isonline=Course.Course_isOnline,
            location=Course.Course_Location,
            begin="default",
            updated="default",
    ):
        # what do the form fields come through as if they're empty? assuming it's None
        if course_name == "" or course_desc == "" or isonline == "" or location == "":
            return ValueError("cannot make a value blank")
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
