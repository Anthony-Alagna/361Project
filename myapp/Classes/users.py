class User:
    User_Id = None
    Email = None
    Type = None
    Name = None
    Phone = None
    Address = None
    ZipCode = None
    City = None
    UserName = None
    isGrader = False

    def __Init__(self, user_id="", email="", type="", name="", phone="", address="", zipCode="",
                 city="", username="", isgrader=""):
        self.User_Id = user_id
        self.Email = email
        self.Type = type
        self.Name = name
        self.Phone = phone
        self.Address = address
        self.ZipCode = zipCode
        self.City = city
        self.UserName = username
        self.isGrader = isgrader

    def get_user_id(self):
        if self.User_Id == "":
            raise TypeError("ID cannot be blank")
        return self.User_Id

    def set_user_id(self, user_id):
        if user_id == "":
            raise TypeError(" user ID cannot be blank")
        self.User_Id = user_id

    def get_email(self):
        if self.Email == "":
            raise TypeError("Email cannot be blank")
        return self.Email

    def set_email(self, email):
        if email == "":
            raise TypeError("email you inputed  cannot be blank")
        self.Email = email

    def get_type(self):
        if self.Type == "":
            raise TypeError("type cannot be blank")
        return self.Type

    def set_type(self, type):
        if type == "":
            raise TypeError("type input cannot be blank")
        self.Type = type

    def get_name(self):
        if self.get_name() == "":
            raise TypeError("name cannot be blank")
        return self.Name

    def set_name(self, name):
        if name == "":
            raise TypeError("name input cannot be blank")
        self.Name = name

    def get_phone(self):
        if self.set_phone() == "":
            raise TypeError("phone cannot be blank")
        return self.Phone

    def set_phone(self, phone):
        if phone == "":
            raise TypeError("phone input cannot be blank")
        self.Phone = phone

    def get_address(self):
        if self.Address == "":
            raise TypeError("address input cannot be blank")
        return self.Address

    def set_address(self, address):
        if address == "":
            raise TypeError("address input cannot be blank")
        self.Address = address

    def get_zipcode(self):
        if self.ZipCode == "":
            raise TypeError("ZipCode cannot be blank")
        return self.ZipCode

    def set_zipcode(self, zipcode):
        if zipcode== "":
            raise TypeError("ZipCode input cannot be blank")
        self.ZipCode = zipcode

    def get_city(self):
        if self.City == "":
            raise TypeError("City cannot be blank")
        return self.City

    def set_city(self, city):
        if city == "":
            raise TypeError("City input cannot be blank")
        self.City = city

    def get_username(self):
        if self.UserName == "":
            raise TypeError("user cannot be blank")
        return self.UserName

    def set_username(self, username):
        if username == "":
            raise TypeError("username input cannot be blank")
        self.UserName = username

    def is_grader(self):
        if self.isGrader == "":
            raise TypeError("username input cannot be blank")
        return self.isGrader

    def set_grader(self, is_grader):
        if is_grader == "":
            raise TypeError("username input cannot be blank")
        self.isGrader = is_grader
