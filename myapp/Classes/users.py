from myapp.models import User, Course, CourseEnrollment
from abc import ABC


class Users(ABC):

    def edit_account(
        self,
        first_name=None,
        last_name=None,
        email=None,
        password=None,
        address=None,
        city=None,
        phone_number=None,
        positions=None
    ):
        if phone_number:
            self.phone_number = phone_number
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if email:
            self.email = email
        if password:
            self.password = password
        if address:
            self.address = address
        if city:
            self.city = city
        if positions:
            self.positions = positions
        if email:
            self.email = email
        self.save()

    def get_user_id(self):
        if self.user_id == "":
            raise TypeError("ID cannot be blank")
        return self.user_id

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

    def getAccountInfo(username, id):
        if username is None:
            raise TypeError("Username cannot be blank")
        if id is None:
            raise TypeError("ID cannot be blank")

        user = User.objects.get(email=username, id=id)
        return user

    def get_user_id(self):
        if self.user_id == "":
            raise TypeError("ID cannot be blank")
        return self.user_id


class UserUtility:
    @staticmethod
    def get_all_users():
        return User.objects.all()
