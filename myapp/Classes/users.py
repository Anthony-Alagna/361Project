from myapp.models import User, Course, CourseEnrollment
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

    def __init__(
        self,
        user_id="",
        email="",
        position="",
        fname="",
        lname="",
        phone="",
        address="",
        city="",
        username="",
        isgrader="",
    ):
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

    def get_user_id(self):
        if self.user_id == "":
            raise TypeError("ID cannot be blank")
        return self.user_id

    def edit_account(
        self,
        fname=None,
        lname=None,
        email=None,
        password=None,
        address=None,
        city=None,
        phone=None,
        position=None
    ):
        if self is type(None) or type(self) is not User:
            raise TypeError("User object is not valid")

        if phone:
            self.phone_number = phone
        if fname:
            self.User_fName = fname
        if lname:
            self.User_lName = lname
        if email:
            self.email = email
        if password:
            self.User_LogPass = password
        if address:
            self.address = address
        if city:
            self.User_City = city
        if fname:
            self.User_fName = fname
        if lname:
            self.User_lName = lname
        if position:
            self.positions = position
        if email:
            self.email = email
        self.save()

    def viewCourse(self, course_id):
        course = Course.objects.get(Course_ID=course_id)
        return course

    def filterUser(usertype):
        if usertype is None:
            return ValueError("you didn't select a usertype")
        elif usertype == "All Roles":
            positionsitions = User.objects.all()
            return positionsitions
        else:
            positionsitions = User.objects.filter(positions=usertype)
            return positionsitions

    def searchUser(last_name):
        if last_name == "":
            return ValueError("You didn't write a last name!")
        # converts parameter to standard case and strips any whitespace before and after characters
        last_name_cleaned = last_name.title().strip()
        # users = User.objects.all()
        if not User.objects.filter(last_name=last_name_cleaned).exists():
            return ValueError("There are no users with this last name")
        user = User.objects.filter(last_name=last_name_cleaned)
        return user

    def viewCourseAssigned(self):
        # how does this retrieve stuff from db?
        courses = CourseToUser.objects.get(user=self)
        return courses

    def getUserByUsername(username):
        if username is None:
            raise TypeError("Username cannot be blank")
        user = User.objects.get(email=username)
        return user


class UserUtility:
    @staticmethod
    def get_all_users():
        return User.objects.all()
