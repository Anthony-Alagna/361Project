from myapp.models import User

class Supervisor(User):
    def createAccount(self, fname, lname, email, username, password, address, city, phone, account_type):
        # what do the form fields come through as if they're empty? assuming it's None
        if fname is None or lname is None or email is None or username is None or password is None or address is None or city is None or phone is None or account_type is None:
            return TypeError(
                "you're missing one of the fields in the form")
        else:
            User.objects.create(User_fName=fname, User_lName=lname, User_Email=email, User_LogName=username,
                                User_LogPass=password, User_Address=address, User_City=city, User_Phone=phone,
                                User_Pos=account_type)
