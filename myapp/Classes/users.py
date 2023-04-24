from myapp.models import User, Section, Course, CourseToUser
import abc


class Users(abc.ABC):
    user_id = None
    email = None
    position = None
    fName = None
    lName = None
    phone = None
    address = None
    city = None
    username = None
    isgrader = False

    def __init__(self, user_id="", email="", position="", fname="", lname="", phone="", address="",
                 city="", username="", isgrader=""):
        self.user_id = user_id
        self.email = email
        self.position = position
        self.fName = fname
        self.lName = lname
        self.phone = phone
        self.address = address
        self.city = city
        self.username = username
        self.isgrader = isgrader

    def getAccountInfo(username, id):
        if username is None:
            raise TypeError("Username cannot be blank")
        if id is None:
            raise TypeError("ID cannot be blank")

        user = User.objects.get(User_LogName=username, id=id)
        return user

    def get_user_id(self):
        if self.user_id == "":
            raise TypeError("ID cannot be blank")
        return self.user_id

    def editInfo(self, phone=None, address=None, city=None, fname=None, lname=None, position=None, email=None):
        if self is type(None) or type(self) is not User:
            raise TypeError("User object is not valid")

        if phone:
            self.User_Phone = phone
        if address:
            self.User_Address = address
        if city:
            self.User_City = city
        if fname:
            self.User_fName = fname
        if lname:
            self.User_lName = lname
        if position:
            self.User_Pos = position
        if email:
            self.User_Email = email

        self.save()

    def viewCourse(self, course_id):
        course = Course.objects.get(Course_ID=course_id)
        return course

    def filterUser(usertype):
        if usertype is None:
            print(usertype)
            return TypeError(
                "you didn't select a usertype")
        elif usertype == "All Roles":
            user_positions = User.objects.all()
            return user_positions
        else:
            user_positions = User.objects.filter(User_Pos=usertype)
            return user_positions

    def searchUser(last_name):
        if last_name == "":
            return TypeError(
                "you didn't select a usertype")
        # converts parameter to standard case and strips any whitespace before and after characters
        last_name_cleaned = last_name.title().strip()
        user = User.objects.filter(User_lName=last_name_cleaned)
        return user

    def viewCourseAssigned(self):
        # how does this retrieve stuff from db?
        courses = CourseToUser.objects.get(user=self)
        return courses


class UserUtility:
    @ staticmethod
    def get_all_users():
        return User.objects.all()
