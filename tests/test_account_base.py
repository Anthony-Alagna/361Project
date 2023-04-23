from django.test import TestCase, Client

from myapp.Classes.supervisor import Supervisor
from myapp.Classes.users import Users, UserUtility
from myapp.models import User


# unit tests for functionality on account base page (searching for user, etc.)

class TestGetUsers(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(id='1', User_Name='Cricket', User_Email='user1@example.com',
                                         User_Type='Teaching Assistant', User_Phone='1234567890',
                                         User_Address='123 Main St',
                                         User_LogName='user1', User_LogPass='password', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')
        self.user2 = User.objects.create(id='2', User_Name='Noodle', User_Email='user2@example.com',
                                         User_Type='Teaching Assistant', User_Phone='0987654321',
                                         User_Address='456 Elm St',
                                         User_LogName='user2', User_LogPass='password1', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-17 00:00:00')
        self.user3 = User.objects.create(id='3', User_Name='Toby', User_Email='user3@example.com',
                                         User_Type='Professor', User_Phone='0987654322', User_Address='457 Elm St',
                                         User_LogName='user3', User_LogPass='password2', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-17 00:00:00')

    def test_get_all_users(self):
        result = UserUtility.get_all_users();
        self.assertEqual(result, User.objects.all(), "get_all_users didn't return all of the users")


# Method: Users.searchUser(username: str)
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
        result = Users.searchUser(username)
        self.assertEqual(result, self.user1, "searchUser has returned the incorrect user")

    # tests if it returns None for a non-existent user
    def test_search_non_existing_user(self):
        username = "uuser1"
        result = Users.searchUser(username)
        self.assertIsNone(result, "searchUser should have returned None")

    # tests if it is not case-sensitive
    def test_search_is_case_insensitive(self):
        username = "USER1"
        result = Users.searchUser(username)
        self.assertEqual(result, self.user1,
                         "searchUser should have returned the username that matches the uppercase parameter")

    # tests if it can handle whitespace
    def test_search_handles_whitespace(self):
        username = "  user1  "
        result = Users.searchUser(username)
        self.assertEqual(result, self.user1, "searchUser should have returned the username that matches the parameter")


# Method: Users.filterUser(usertype: str)
class TestFilterUser(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(id='1', User_Name='Cricket', User_Email='user1@example.com',
                                         User_Type='Teaching Assistant', User_Phone='1234567890',
                                         User_Address='123 Main St',
                                         User_LogName='user1', User_LogPass='password', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')
        self.user2 = User.objects.create(id='2', User_Name='Noodle', User_Email='user2@example.com',
                                         User_Type='Teaching Assistant', User_Phone='0987654321',
                                         User_Address='456 Elm St',
                                         User_LogName='user2', User_LogPass='password1', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-17 00:00:00')
        self.user3 = User.objects.create(id='3', User_Name='Toby', User_Email='user3@example.com',
                                         User_Type='Professor', User_Phone='0987654322', User_Address='457 Elm St',
                                         User_LogName='user3', User_LogPass='password2', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-17 00:00:00')

    def test_filter_user_TA(self):
        usertype = "Teaching Assistant"
        result = Users.filterUser(usertype)
        self.assertEqual(result, [self.user1, self.user2],
                         "filterUser didn't return all of the TA users")

    def test_filter_user_Professor(self):
        usertype = "Professor"
        result = Users.filterUser(usertype)
        self.assertEqual(result, [self.user3],
                         "filterUser didn't return all of the Professor users")

    def test_filter_all_user(self):
        usertype = "All Roles"
        result = Users.filterUser(usertype)
        self.assertEqual(result, User.objects.all(),
                         "filterUser didn't return all the users")

    def test_filter_no_user(self):
        usertype = None
        result = Users.filterUser(usertype)
        self.assertEqual(result, None, "filterUser should have returned None")


# Method: Supervisor.deleteUser(username: str)
class TestDeleteUser(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(id='1', User_Name='Cricket', User_Email='user1@example.com',
                                         User_Type='TA', User_Phone='1234567890', User_Address='123 Main St',
                                         User_LogName='user1', User_LogPass='password', User_isGrader='no',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')

    def test_delete_user(self):
        username = "user1"

        Supervisor.deleteUser(username)

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

    # click on the home button
    def test_go_home_view(self):
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)

    # click on the delete button
    def test_delete_account_view(self):
        response = self.client.get('/accountbase/')
        self.assertEqual(response.status_code, 200)

    # click on the filter button
    def test_filter_account_view(self):
        response = self.client.get('/accountbase/')
        self.assertEqual(response.status_code, 200)

    # click on the search button
    def test_search_account_view(self):
        response = self.client.get('/accountbase/')
        self.assertEqual(response.status_code, 200)

    # click on the edit button
    def test_edit_account_view(self):
        response = self.client.get('/editaccount/')
        self.assertEqual(response.status_code, 200)
