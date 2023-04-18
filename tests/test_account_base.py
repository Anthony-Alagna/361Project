from django.test import TestCase, Client
from myapp.models import User


# unit tests for functionality on account base page (searching for user, etc.)

# methods I'll be creating tests for

# Account.getAccountInfo (username:str)

# Account.getUser()

# Account.searchUser(username: str)

# Account.getAccountInfo (username:str)

# methods that need to added to LL design

# 1. some sort of filter for the drop down roles tab, that will filter users by TA or Instructor
# 2. method that takes user to the create account page if they click create new account
# 3. method that takes user to the user's current account page if they click on the hyperlinked user name
# 4. method that takes user to the user's current account page, in edit mode if they click the edit icon button
# 5. method that takes user to homepage if they click on home button
# 6. method that logs user out if they click on logout button
# 7. method that deletes user account if they click the delete icon button
