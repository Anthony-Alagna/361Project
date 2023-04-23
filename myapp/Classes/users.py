import myapp.models
from myapp.models import User, Section, Course, CourseToUser
import abc


class Users(abc.ABC):
    user_id = None
    email = None
    Position = None
    fName = None
    lName = None
    phone = None
    address = None
    city = None
    username = None
    isgrader = False

    def __Init__(self, user_id="", email="", position="", fname="", lname="", phone="", address="",
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

    def getAccountInfo(self, username, id):
        if self.username == username and self.user_id == id:
            user = User.objects.get(User_Name=username)
            return user.User_fName, user.User_lName, user.User_LogName, user.User_Email, user.User_Pos
        else:
            return Exception("user not in the database")

    def get_user_id(self):
        if self.user_id == "":
            raise TypeError("ID cannot be blank")
        return self.user_id

    def editInfo(self, phone, address, city, fname, lname):
        if phone != "":
            self.phone = phone
            nPhone = User.objects.get(User_Phone=self.phone)
            nPhone.phone = phone
            nPhone.save()
        if address != "":
            self.address = address
            nAddress = User.objects.get(User_Address=self.address)
            nAddress.address = address
            nAddress.save()
        if city != "":
            self.city = city
            nCity = User.objects.get(User_City=self.city)
            nCity.city = city
            nCity.save()

        if fname != "":
            self.fName = fname
            name = User.objects.get(User_fName=self.fName)
            name.User_fName = fname
            name.save()
        if lname != "":
            self.lName = lname
            lastn = User.objects.get(User_lName=self.lName)
            lastn.User_lName = lname
            lastn.save()

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
        if last_name is "":
            return TypeError(
                "you didn't select a usertype")
        # converts parameter to standard case and strips any whitespace before and after characters
        last_name_cleaned = last_name.title().strip()
        user = User.objects.filter(User_lName=last_name_cleaned)
        return user

    def viewCourseAssigned(self):
        course_for_user = []
        # how does this retrieve stuff from db?
        courses = CourseToUser.objects.get(user=self)
        return courses


class UserUtility:
    @staticmethod
    def get_all_users():
        return User.objects.all()
