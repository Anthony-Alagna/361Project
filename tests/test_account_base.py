from django.test import TestCase, Client
from myapp.models import User
from myapp.views import AccountBase


# unit tests for functionality on account base page (searching for user, etc.)
# using User as class for methods until Account class is added to project

# Method: Account.searchUser(username: str)
class TestSearchUser(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(id='1', User_Name='Cricket', User_Email='user1@example.com',
                                         User_Type='TA', User_Phone='1234567890', User_Address='123 Main St',
                                         User_LogName='user1', User_LogPass='password', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')
        self.user2 = User.objects.create(id='2', User_Name='Noodle', User_Email='user2@example.com',
                                         User_Type='TA', User_Phone='0987654321', User_Address='456 Elm St',
                                         User_LogName='user2', User_LogPass='password1', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-17 00:00:00')

    # tests if it returns the correct user
    def test_search_existing_user(self):
        username = "user1"
        result = AccountBase.searchUser(username)
        self.assertEqual(result, self.user1, "searchUser has returned the incorrect user")

    # tests if it returns None for a non-existent user
    def test_search_non_existing_user(self):
        username = "uuser1"
        result = AccountBase.searchUser(username)
        self.assertIsNone(result, "searchUser should have returned None")

    # tests if it is not case-sensitive
    def test_search_is_case_insensitive(self):
        username = "USER1"
        result = AccountBase.searchUser(username)
        self.assertEqual(result, self.user1,
                         "searchUser should have returned the username that matches the uppercase parameter")

    # tests if it can handle whitespace
    def test_search_handles_whitespace(self):
        username = "  user1  "
        result = AccountBase.searchUser(username)
        self.assertEqual(result, self.user1, "searchUser should have returned the username that matches the parameter")


# Account.filterUser(usertype: str)
class TestFilterUser(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(id='1', User_Name='Cricket', User_Email='user1@example.com',
                                         User_Type='TA', User_Phone='1234567890', User_Address='123 Main St',
                                         User_LogName='user1', User_LogPass='password', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')
        self.user2 = User.objects.create(id='2', User_Name='Noodle', User_Email='user2@example.com',
                                         User_Type='TA', User_Phone='0987654321', User_Address='456 Elm St',
                                         User_LogName='user2', User_LogPass='password1', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-17 00:00:00')
        self.user3 = User.objects.create(id='3', User_Name='Toby', User_Email='user3@example.com',
                                         User_Type='Professor', User_Phone='0987654322', User_Address='457 Elm St',
                                         User_LogName='user3', User_LogPass='password2', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-17 00:00:00')

    def test_filter_user_TA(self):
        usertype = "TA"
        result = AccountBase.filterUser(usertype)
        self.assertEqual(result, [self.user1, self.user2],
                         "filterUser didn't return all of the TA users")

    def test_filter_user_Professor(self):
        usertype = "Professor"
        result = AccountBase.filterUser(usertype)
        self.assertEqual(result, [self.user3],
                         "filterUser didn't return all of the Professor users")

    def test_filter_all_user(self):
        usertype = "All Roles"
        result = AccountBase.filterUser(usertype)
        self.assertEqual(result, [self.user1, self.user2, self.user3],
                         "filterUser didn't return all the users")


# Account.deleteUser(username: str)
class TestDeleteUser(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(id='1', User_Name='Cricket', User_Email='user1@example.com',
                                         User_Type='TA', User_Phone='1234567890', User_Address='123 Main St',
                                         User_LogName='user1', User_LogPass='password', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')

    def test_delete_user(self):
        username = "user1"

        User.deleteUser(username)

        self.assertFalse(User.objects.filter(User_LogName="user1").exists(), "User exists but they were deleted")


# tests all the navigation functionality on the page
class TestButtons(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create(id='1', User_Name='Cricket', User_Email='user1@example.com',
                                         User_Type='TA', User_Phone='1234567890', User_Address='123 Main St',
                                         User_LogName='user1', User_LogPass='password', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')

    # click create new account button
    def test_create_new_account_view(self):
        response = self.client.get('/createaccount/')
        self.assertEqual(response.status_code, 200)

    # click on the hyperlinked username
    def test_user_account_view(self):
        response = self.client.get(f'/account/{self.user1.User_Name}')
        self.assertEqual(response.status_code, 200)

    # click on the edit icon button
    def test_edit_account_view(self):
        response = self.client.get(f'/editaccount/{self.user1.User_Name}')
        self.assertEqual(response.status_code, 200)

    # click on the home button
    def test_go_home_view(self):
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
