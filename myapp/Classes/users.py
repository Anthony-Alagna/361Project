import myapp.models
from myapp.models import User, Section, Course, CourseToUser


class User:
    user_id = None
    email = None
    type = None
    name = None
    phone = None
    address = None
    city = None
    username = None
    isgrader = False

    def __Init__(self, user_id="", email="", type="", name="", phone="", address="",
                 city="", username="", isgrader=""):
        self.user_id = user_id
        self.email = email
        self.type = type
        self.name = name
        self.phone = phone
        self.address = address
        self.city = city
        self.username = username
        self.isgrader = isgrader

    def get_user_id(self):
        if self.user_id == "":
            raise TypeError("ID cannot be blank")
        return self.user_id

    def set_user_id(self, user_id):
        if user_id == "":
            raise TypeError(" user ID cannot be blank")
        self.user_id = user_id
        id = User.objects.get(id=self.id)
        id.id = user_id
        id.save()

    def get_email(self):
        if self.email == "":
            raise TypeError("Email cannot be blank")
        return self.email

    def set_email(self, email):
        if email == "":
            raise TypeError("email you inputed  cannot be blank")
        # is this the right way to edit the users attributes in the model
        user_email = User.objects.get(User_Email=self.email)
        user_email.email = email
        self.email = email
        user_email.save()

    def get_type(self):
        if self.type == "":
            raise TypeError("type cannot be blank")
        return self.type

    def set_type(self, type):
        if type == "":
            raise TypeError("type input cannot be blank")
        self.type = type
        user_type = User.objects.get(User_Email=self.type)
        user_type.type = type
        user_type.save()

    def get_name(self):
        if self.get_name() == "":
            raise TypeError("name cannot be blank")
        return self.Name

    def set_name(self, name):
        if name == "":
            raise TypeError("name input cannot be blank")
        self.name = name
        nName = User.objects.get(User_Email=self.name)
        nName.name = name
        nName.save()

    def get_phone(self):
        if self.phone == "":
            raise TypeError("phone cannot be blank")
        return self.phone

    def set_phone(self, phone):
        if phone == "":
            raise TypeError("phone input cannot be blank")
        self.phone = phone
        nPhone = User.objects.get(User_Email=self.email)
        nPhone.phone = phone
        nPhone.save()

    def get_address(self):
        if self.address == "":
            raise TypeError("address input cannot be blank")
        return self.address

    def set_address(self, address):
        if address == "":
            raise TypeError("address input cannot be blank")
        self.address = address
        nAddress = User.objects.get(User_Email=self.email)
        nAddress.address = address
        nAddress.save()

    def get_zipcode(self):
        if self.ZipCode == "":
            raise TypeError("ZipCode cannot be blank")
        return self.ZipCode

    def get_city(self):
        if self.city == "":
            raise TypeError("City cannot be blank")
        return self.city

    def set_city(self, city):
        if city == "":
            raise TypeError("City input cannot be blank")
        self.city = city
        nCity = User.objects.get(User_Email=self.email)
        nCity.city = city
        nCity.save()

    def get_username(self):
        if self.username == "":
            raise TypeError("user cannot be blank")
        return self.username

    def set_username(self, username):
        if username == "":
            raise TypeError("username input cannot be blank")
        self.username = username
        nUsername = User.objects.get(User_Email=self.email)
        nUsername.username = username
        nUsername.save()

    # gotta fgure out how to implement functions below
    #
    # def getAssignment(self):
    #
    # #model for user makes sure username is unique for each user
    # def searchUser(self, username):
    # def filterUser(self, type):
    #
    # def viewCourses(self):
