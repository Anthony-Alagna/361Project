from django.test import TestCase, Client
from myapp.models import User


# unit tests for functionality on account base page (searching for user, etc.)

# Method: Account.searchUser(username: str)
class TestSearchUser(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(User_ID='1', User_Name='Cricket', User_Email='user1@example.com',
                                         User_Type='student', User_Phone='1234567890', User_Address='123 Main St',
                                         User_LogName='user1', User_LogPass='password', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')
        self.user2 = User.objects.create(User_ID='2', User_Name='Noodle', User_Email='user2@example.com',
                                         User_Type='student', User_Phone='0987654321', User_Address='456 Elm St',
                                         User_LogName='user2', User_LogPass='password1', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-17 00:00:00')

    # tests if it returns the correct user
    def test_search_existing_user(self):
        username = "user1"
        result = User.searchUser(username)
        self.assertEqual(result, self.user1, "searchUser has returned the incorrect user")

    # tests if it returns None for a non-existent user
    def test_search_non_existing_user(self):
        username = "uuser1"
        result = User.searchUser(username)
        self.assertIsNone(result, "searchUser should have returned None")

    # tests if it is not case-sensitive
    def test_search_is_case_insensitive(self):
        username = "USER1"
        result = User.searchUser(username)
        self.assertEqual(result, self.user1,
                         "searchUser should have returned the username that matches the uppercase parameter")

    # tests if it can handle whitespace
    def test_search_handles_whitespace(self):
        username = "  user1  "
        result = User.searchUser(username)
        self.assertEqual(result, self.user1, "searchUser should have returned the username that matches the parameter")

# methods I'll be creating tests for

# Account.getAccountInfo (username:str)

# Account.getUser()


# Account.getAccountInfo (username:str)

# methods that need to added to LL design

# 1. some sort of filter for the drop down roles tab, that will filter users by TA or Instructor
# 6. method that logs user out if they click on logout button
# 7. method that deletes user account if they click the delete icon button


# these will all just be embedded within html (my brain is thinking we're using Javascript but we're not)
# 2. method that takes user to the create account page if they click create new account
# 3. method that takes user to the user's current account page if they click on the hyperlinked user name
# 4. method that takes user to the user's current account page, in edit mode if they click the edit icon button
# 5. method that takes user to homepage if they click on home button
