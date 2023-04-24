from django.test import TestCase, Client
from django.urls import reverse

from myapp.Classes.supervisor import Supervisor
from myapp.Classes.users import Users, UserUtility
from myapp.models import User


# unit tests for functionality on account base page (searching for user, etc.)

class TestGetUsers(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(id='1', User_fName='Cricket', User_lName="Maule",
                                         User_Email='user1@example.com',
                                         User_Pos='Teaching Assistant', User_Phone='1234567890',
                                         User_Address='123 Main St', User_City="Milwaukee",
                                         User_LogName='user1', User_LogPass='password',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')
        self.user2 = User.objects.create(id='2', User_fName='Noodle', User_lName="Bannish",
                                         User_Email='user2@example.com',
                                         User_Pos='Teaching Assistant', User_Phone='0987654321',
                                         User_Address='456 Elm St', User_City="Milwaukee",
                                         User_LogName='user2', User_LogPass='password1',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-17 00:00:00')
        self.user3 = User.objects.create(id='3', User_fName='Toby', User_lName="Smith", User_Email='user3@example.com',
                                         User_Pos='Instructor', User_Phone='0987654322', User_Address='457 Elm St',
                                         User_City="Milwaukee", User_LogName='user3', User_LogPass='password2',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-17 00:00:00')


# Method: UserUtility.get_all_users()
class TestGetAllUsers(TestCase):

    def test_get_all_users(self):
        result = UserUtility.get_all_users()
        self.assertEqual(list(result), list(User.objects.all()),
                         "get_all_users didn't return all of the users")


# Method: Users.searchUser(username: str)
class TestSearchUser(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(id='1', User_fName='Cricket', User_lName="Maule",
                                         User_Email='user1@example.com',
                                         User_Pos='Teaching Assistant', User_Phone='1234567890',
                                         User_Address='123 Main St', User_City="Milwaukee",
                                         User_LogName='user1', User_LogPass='password',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')
        self.user2 = User.objects.create(id='2', User_fName='Noodle', User_lName="Bannish",
                                         User_Email='user2@example.com',
                                         User_Pos='Teaching Assistant', User_Phone='0987654321',
                                         User_Address='456 Elm St', User_City="Milwaukee",
                                         User_LogName='user2', User_LogPass='password1',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-17 00:00:00')
        self.user3 = User.objects.create(id='3', User_fName='Toby', User_lName="Smith", User_Email='user3@example.com',
                                         User_Pos='Instructor', User_Phone='0987654322', User_Address='457 Elm St',
                                         User_City="Milwaukee", User_LogName='user3', User_LogPass='password2',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-17 00:00:00')

    # tests if it returns the correct user
    def test_search_existing_user(self):
        last_name = "Maule"
        result = Users.searchUser(last_name)
        self.assertEqual(list(result), list(User.objects.filter(User_lName="Maule")),
                         "searchUser has returned the incorrect user")

    # tests if it returns None for a non-existent user
    def test_search_non_existing_user(self):
        last_name = "Mauule"
        result = Users.searchUser(last_name)
        self.assertEqual(isinstance(result, TypeError), True,
                         "searchUser should have returned no users")

        # tests if it returns None for a non-existent user

    def test_search_no_user(self):
        last_name = ""
        result = Users.searchUser(last_name)
        self.assertEqual(isinstance(result, TypeError), True,
                         "searchUser should have returned no users")

    # tests if it is not case-sensitive
    def test_search_is_case_insensitive(self):
        last_name = "MAULE"
        result = Users.searchUser(last_name)
        self.assertEqual(list(result), list(User.objects.filter(User_lName="Maule")),
                         "searchUser should have returned the username that matches the uppercase parameter")

    # tests if it can handle whitespace
    def test_search_handles_whitespace(self):
        last_name = "  Maule  "
        result = Users.searchUser(last_name)
        self.assertEqual(list(result), list(User.objects.filter(User_lName="Maule")),
                         "searchUser should have returned the username that matches the parameter")


# Method: Users.filterUser(usertype: str)
class TestFilterUser(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(id='1', User_fName='Cricket', User_lName="Maule",
                                         User_Email='user1@example.com',
                                         User_Pos='Teaching Assistant', User_Phone='1234567890',
                                         User_Address='123 Main St', User_City="Milwaukee",
                                         User_LogName='user1', User_LogPass='password',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')
        self.user2 = User.objects.create(id='2', User_fName='Noodle', User_lName="Bannish",
                                         User_Email='user2@example.com',
                                         User_Pos='Teaching Assistant', User_Phone='0987654321',
                                         User_Address='456 Elm St', User_City="Milwaukee",
                                         User_LogName='user2', User_LogPass='password1',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-17 00:00:00')
        self.user3 = User.objects.create(id='3', User_fName='Toby', User_lName="Smith", User_Email='user3@example.com',
                                         User_Pos='Instructor', User_Phone='0987654322', User_Address='457 Elm St',
                                         User_City="Milwaukee", User_LogName='user3', User_LogPass='password2',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-17 00:00:00')

    def test_filter_user_TA(self):
        usertype = "Teaching Assistant"
        result = Users.filterUser(usertype)
        self.assertEqual(list(result), list(User.objects.filter(User_Pos="Teaching Assistant")),
                         "filterUser didn't return all of the TA users")

    def test_filter_user_Instructor(self):
        usertype = "Instructor"
        result = Users.filterUser(usertype)
        self.assertEqual(list(result), list(User.objects.filter(User_Pos="Instructor")),
                         "filterUser didn't return all of the Instructor users")

    def test_filter_all_user(self):
        usertype = "All Roles"
        result = Users.filterUser(usertype)
        self.assertEqual(list(result), list(User.objects.all()),
                         "filterUser didn't return all the users")

    def test_filter_no_user(self):
        usertype = None
        result = Users.filterUser(usertype)
        self.assertEqual(isinstance(result, TypeError), True,
                         "filterUser should have returned None")


# Method: Supervisor.deleteUser(username: str)
class TestDeleteUser(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(id='1', User_fName='Cricket', User_lName="Maule",
                                         User_Email='user1@example.com',
                                         User_Pos='Teaching Assistant', User_Phone='1234567890',
                                         User_Address='123 Main St', User_City="Milwaukee",
                                         User_LogName='user1', User_LogPass='password',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00')
        self.user2 = User.objects.create(id='2', User_fName='Noodle', User_lName="Bannish",
                                         User_Email='user2@example.com',
                                         User_Pos='Teaching Assistant', User_Phone='0987654321',
                                         User_Address='456 Elm St', User_City="Milwaukee",
                                         User_LogName='user2', User_LogPass='password1',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-17 00:00:00')
        self.user3 = User.objects.create(id='3', User_fName='Toby', User_lName="Smith", User_Email='user3@example.com',
                                         User_Pos='Instructor', User_Phone='0987654322', User_Address='457 Elm St',
                                         User_City="Milwaukee", User_LogName='user3', User_LogPass='password2',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-17 00:00:00')

    def test_delete_user(self):
        username = "user1"

        Supervisor.deleteUser(username)

        self.assertFalse(User.objects.filter(
            User_LogName="user1").exists(), "User exists but they were deleted")


# tests all the navigation functionality on the page
class TestButtons(TestCase):
    def setUp(self):
        self.client = Client()

    # click create new account button
    def test_create_new_account_view(self):
        response = self.client.get(reverse('createaccount'))
        self.assertEqual(response.status_code, 200)

    # click on the home button
    def test_go_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    # click on the delete button
    def test_delete_account_view(self):
        response = self.client.get(reverse('accountbase'))
        self.assertEqual(response.status_code, 200)

    # click on the filter button
    def test_filter_account_view(self):
        response = self.client.get(reverse('accountbase'))
        self.assertEqual(response.status_code, 200)

    # click on the search button
    def test_search_account_view(self):
        response = self.client.get(reverse('accountbase'))
        self.assertEqual(response.status_code, 200)

    # click on the edit button
    def test_edit_account_view(self):
        response = self.client.get(reverse('editaccount'))
        self.assertEqual(response.status_code, 200)
