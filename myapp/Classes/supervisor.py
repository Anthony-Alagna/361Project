from myapp.models import User, Course


def checkInstructorInCourse(self, instructor_name, course_id):
    if instructor_name is None or course_id is None:
        return TypeError("instructor name is blank or course id name is blank")
    else:
        course = Course.objects.get(Course_ID=course_id)
        if course is None:
            return TypeError("the course you search does not exist")
        elif course.Course_Instructor is not None:
            return TypeError("you must remove instructor before you can add new one")
        else:
            return True


class Supervisor(User):
    @staticmethod
    def create_account(fname, lname, email, username, password, address, city, phone, account_type):
        # what do the form fields come through as if they're empty? assuming it's None
        if fname is "" or lname is ""  or email is ""  or username is ""  or password is ""  or address is ""  or city is ""  or phone is ""  or account_type is "" :
            return TypeError(
                "missing field")

        else:
            User.objects.create(User_fName=fname, User_lName=lname, User_Email=email, User_LogName=username,
                                User_LogPass=password, User_Address=address, User_City=city, User_Phone=phone,
                                User_Pos=account_type)
    @staticmethod
    def removeInstructorFromClass(instructor_name, course_id):
        if not checkInstructorInCourse(instructor_name, course_id):
            return TypeError("instructor name is blank or course id name is blank")
        else:
            course = Course.objects.get(Course_ID=course_id)
            course.Course_Instructor = ""
            course.save()
            return course

    @staticmethod
    def addInstructor(instructor_name, course_id):
        if not checkInstructorInCourse(instructor_name, course_id):
            return TypeError("error cannot add instructor")
        else:
            course = Course.objects.get(Course_ID=course_id)
            course.Course_Instructor = instructor_name
            course.save()
            return course

    def deleteUser(username):
        user = User.objects.filter(User_LogName=username)
        user.delete()

