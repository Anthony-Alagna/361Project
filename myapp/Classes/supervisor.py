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
        if fname is None or lname is None or email is None or username is None or password is None or address is None or city is None or phone is None or account_type is None:
            return TypeError(
                "you're missing one of the fields in the form")
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
