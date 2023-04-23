from myapp.Classes.users import Users
from myapp.models import User


class Supervisor(Users):
    @staticmethod
    def create_account(fname, lname, email, username, password, address, city, phone, account_type):
        users = User.objects.all()
        for user in users:
            if user.User_LogName == username:
                return TypeError(
                    "username already exists")

        if fname is "" or lname is "" or email is "" or username is "" or password is "" or address is "" or city is "" or phone is "" or account_type is "":
            return TypeError(
                "missing field")

        else:
            user = User.objects.create(User_fName=fname, User_lName=lname, User_Email=email, User_LogName=username,
                                       User_LogPass=password, User_Address=address, User_City=city, User_Phone=phone,
                                       User_Pos=account_type)
            print(user.User_LogName)
            return user

    def deleteUser(username):
        user = User.objects.filter(User_LogName=username)
        user.delete()
