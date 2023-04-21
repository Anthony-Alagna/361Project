import myapp.models
from myapp.models import Section,Course, courseToUser

class User:
    user_id = None
    email = None
    type = None
    name = None
    phone= None
    address = None
    zipcode = None
    city = None
    username = None
    isgrader = False

    def __Init__(self, user_id="", email="", type="", name="", phone="", address="", zipCode="",
                 city="", username="", isgrader=""):
        self.user_id = user_id
        self.email = email
        self.type = type
        self.name = name
        self.phone = phone
        self.address = address
        self.zipcode= zipCode
        self.city= city
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

    def get_email(self):
        if self.email == "":
            raise TypeError("Email cannot be blank")
        return self.email

    def set_email(self, email):
        if email == "":
            raise TypeError("email you inputed  cannot be blank")
        user_email = myapp.objects.get(User_Email=email)
        user_email=email
        self.email = email

    def get_type(self):
        if self.type == "":
            raise TypeError("type cannot be blank")
        return self.type

    def set_type(self, type):
        if type == "":
            raise TypeError("type input cannot be blank")

        self.type = type

    def get_name(self):
        if self.get_name() == "":
            raise TypeError("name cannot be blank")
        return self.Name

    def set_name(self, name):
        if name == "":
            raise TypeError("name input cannot be blank")
        self.name = name

    def get_phone(self):
        if self.phone == "":
            raise TypeError("phone cannot be blank")
        return self.phone

    def set_phone(self, phone):
        if phone == "":
            raise TypeError("phone input cannot be blank")
        self.phone = phone

    def get_address(self):
        if self.address == "":
            raise TypeError("address input cannot be blank")
        return self.address

    def set_address(self, address):
        if address == "":
            raise TypeError("address input cannot be blank")
        self.address = address

    def get_zipcode(self):
        if self.ZipCode == "":
            raise TypeError("ZipCode cannot be blank")
        return self.ZipCode

    def set_zipcode(self, zipcode):
        if zipcode== "":
            raise TypeError("ZipCode input cannot be blank")
        self.zipcode = zipcode

    def get_city(self):
        if self.city == "":
            raise TypeError("City cannot be blank")
        return self.city

    def set_city(self, city):
        if city == "":
            raise TypeError("City input cannot be blank")
        self.city = city

    def get_username(self):
        if self.username == "":
            raise TypeError("user cannot be blank")
        return self.username

    def set_username(self, username):
        if username == "":
            raise TypeError("username input cannot be blank")
        self.username = username

    def is_grader(self):
        if self.isgrader == "":
            raise TypeError("username input cannot be blank")
        return self.isgrader

    def set_grader(self, is_grader):
        if is_grader == "":
            raise TypeError("username input cannot be blank")
        self.isgrader = is_grader

    def course_to_User(self, course, section):
        course = myapp.models.courseToUser(Course_Name=course)