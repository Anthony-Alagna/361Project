from django.test import TestCase, Client
from django.urls import reverse

from myapp.Classes.supervisor import Supervisor
from myapp.Classes.users import Users, UserUtility
from myapp.models import User


# unit tests for functionality on account base page (searching for user, etc.)


class TestGetUsers(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            id="1",
            first_name="Cricket",
            last_name="Maule",
            email="user1@example.com",
            positions="Teaching Assistant",
            phone_number="1234567890",
            address="123 Main St",
            city="Milwaukee",
            password="password",
            created_at="2022-01-01 00:00:00",
            updated_at="2023-04-18 00:00:00",
        )
        self.user2 = User.objects.create(
            id="2",
            first_name="Noodle",
            last_name="Bannish",
            email="user2@example.com",
            positions="Teaching Assistant",
            phone_number="0987654321",
            address="456 Elm St",
            city="Milwaukee",
            password="password1",
            created_at="2022-01-01 00:00:00",
            updated_at="2023-04-17 00:00:00",
        )
        self.user3 = User.objects.create(
            id="3",
            first_name="Toby",
            last_name="Smith",
            email="user3@example.com",
            positions="Instructor",
            phone_number="0987654322",
            address="457 Elm St",
            city="Milwaukee",
            password="password2",
            created_at="2022-01-01 00:00:00",
            updated_at="2023-04-17 00:00:00",
        )

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()
        self.user3.delete()


# Method: UserUtility.get_all_users()
class TestGetAllUsers(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            id="1",
            first_name="Cricket",
            last_name="Maule",
            email="user1@example.com",
            positions="Teaching Assistant",
            phone_number="1234567890",
            address="123 Main St",
            city="Milwaukee",
            password="password",
            created_at="2022-01-01 00:00:00",
            updated_at="2023-04-18 00:00:00",
        )
        self.user2 = User.objects.create(
            id="2",
            first_name="Noodle",
            last_name="Bannish",
            email="user2@example.com",
            positions="Teaching Assistant",
            phone_number="0987654321",
            address="456 Elm St",
            city="Milwaukee",
            password="password1",
            created_at="2022-01-01 00:00:00",
            updated_at="2023-04-17 00:00:00",
        )
        self.user3 = User.objects.create(
            id="3",
            first_name="Toby",
            last_name="Smith",
            email="user3@example.com",
            positions="Instructor",
            phone_number="0987654322",
            address="457 Elm St",
            city="Milwaukee",
            password="password2",
            created_at="2022-01-01 00:00:00",
            updated_at="2023-04-17 00:00:00",
        )

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()
        self.user3.delete()

    def test_get_all_users(self):
        result = UserUtility.get_all_users()
        self.assertEqual(
            list(result),
            list(User.objects.all()),
            "get_all_users didn't return all of the users",
        )


# Method: Users.searchUser(username: str)
class TestSearchUser(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            id="1",
            first_name="Cricket",
            last_name="Maule",
            email="user1@example.com",
            positions="Teaching Assistant",
            phone_number="1234567890",
            address="123 Main St",
            city="Milwaukee",
            password="password",
            created_at="2022-01-01 00:00:00",
            updated_at="2023-04-18 00:00:00",
        )
        self.user2 = User.objects.create(
            id="2",
            first_name="Noodle",
            last_name="Bannish",
            email="user2@example.com",
            positions="Teaching Assistant",
            phone_number="0987654321",
            address="456 Elm St",
            city="Milwaukee",
            password="password1",
            created_at="2022-01-01 00:00:00",
            updated_at="2023-04-17 00:00:00",
        )
        self.user3 = User.objects.create(
            id="3",
            first_name="Toby",
            last_name="Smith",
            email="user3@example.com",
            positions="Instructor",
            phone_number="0987654322",
            address="457 Elm St",
            city="Milwaukee",
            password="password2",
            created_at="2022-01-01 00:00:00",
            updated_at="2023-04-17 00:00:00",
        )

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()
        self.user3.delete()

    # tests if it returns the correct user
    def test_search_existing_user(self):
        last_name = "Maule"
        result = Users.searchUser(last_name)
        self.assertEqual(
            list(result),
            list(User.objects.filter(last_name="Maule")),
            "searchUser has returned the incorrect user",
        )

    # tests if it returns None for a non-existent user
    def test_search_non_existing_user(self):
        last_name = "Mauule"
        result = Users.searchUser(last_name)
        self.assertEqual(
            isinstance(result, ValueError),
            True,
            "searchUser should have returned no users",
        )

        # tests if it returns None for a non-existent user

    def test_search_no_user(self):
        last_name = ""
        result = Users.searchUser(last_name)
        self.assertEqual(
            isinstance(result, ValueError),
            True,
            "searchUser should have returned no users",
        )

    # tests if it is not case-sensitive
    def test_search_is_case_insensitive(self):
        last_name = "MAULE"
        result = Users.searchUser(last_name)
        self.assertEqual(
            list(result),
            list(User.objects.filter(last_name="Maule")),
            "searchUser should have returned the username that matches the uppercase parameter",
        )

    # tests if it can handle whitespace
    def test_search_handles_whitespace(self):
        last_name = "  Maule  "
        result = Users.searchUser(last_name)
        self.assertEqual(
            list(result),
            list(User.objects.filter(last_name="Maule")),
            "searchUser should have returned the username that matches the parameter",
        )


# Method: Users.filterUser(usertype: str)
class TestFilterUser(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            id="1",
            first_name="Cricket",
            last_name="Maule",
            email="user1@example.com",
            positions="Teaching Assistant",
            phone_number="1234567890",
            address="123 Main St",
            city="Milwaukee",
            password="password",
            created_at="2022-01-01 00:00:00",
            updated_at="2023-04-18 00:00:00",
        )
        self.user2 = User.objects.create(
            id="2",
            first_name="Noodle",
            last_name="Bannish",
            email="user2@example.com",
            positions="Teaching Assistant",
            phone_number="0987654321",
            address="456 Elm St",
            city="Milwaukee",
            password="password1",
            created_at="2022-01-01 00:00:00",
            updated_at="2023-04-17 00:00:00",
        )
        self.user3 = User.objects.create(
            id="3",
            first_name="Toby",
            last_name="Smith",
            email="user3@example.com",
            positions="Instructor",
            phone_number="0987654322",
            address="457 Elm St",
            city="Milwaukee",
            password="password2",
            created_at="2022-01-01 00:00:00",
            updated_at="2023-04-17 00:00:00",
        )

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()
        self.user3.delete()

    def test_filter_user_TA(self):
        usertype = "Teaching Assistant"
        result = Users.filterUser(usertype)
        self.assertEqual(
            list(result),
            list(User.objects.filter(positions="Teaching Assistant")),
            "filterUser didn't return all of the TA users",
        )

    def test_filter_user_Instructor(self):
        usertype = "Instructor"
        result = Users.filterUser(usertype)
        self.assertEqual(
            list(result),
            list(User.objects.filter(positions="Instructor")),
            "filterUser didn't return all of the Instructor users",
        )

    def test_filter_all_user(self):
        usertype = "All Roles"
        result = Users.filterUser(usertype)
        self.assertEqual(
            list(result),
            list(User.objects.all()),
            "filterUser didn't return all the users",
        )

    def test_filter_no_user(self):
        usertype = None
        result = Users.filterUser(usertype)
        self.assertEqual(
            isinstance(
                result, ValueError), True, "filterUser should have returned None"
        )


# Method: Supervisor.deleteUser(username: str)
class TestDeleteUser(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            id="1",
            first_name="Cricket",
            last_name="Maule",
            email="user1@example.com",
            positions="Teaching Assistant",
            phone_number="1234567890",
            address="123 Main St",
            city="Milwaukee",
            password="password",
            created_at="2022-01-01 00:00:00",
            updated_at="2023-04-18 00:00:00",
        )
        self.user2 = User.objects.create(
            id="2",
            first_name="Noodle",
            last_name="Bannish",
            email="user2@example.com",
            positions="Teaching Assistant",
            phone_number="0987654321",
            address="456 Elm St",
            city="Milwaukee",
            password="password1",
            created_at="2022-01-01 00:00:00",
            updated_at="2023-04-17 00:00:00",
        )
        self.user3 = User.objects.create(
            id="3",
            first_name="Toby",
            last_name="Smith",
            email="user3@example.com",
            positions="Instructor",
            phone_number="0987654322",
            address="457 Elm St",
            city="Milwaukee",
            password="password2",
            created_at="2022-01-01 00:00:00",
            updated_at="2023-04-17 00:00:00",
        )

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()
        self.user3.delete()

    def test_delete_user(self):
        username = "user1@example.com"

        Supervisor.deleteUser(username)

        self.assertFalse(
            User.objects.filter(email="user1@example.com").exists(),
            "User exists but they were deleted",
        )


# tests all the navigation functionality on the page
class TestButtons(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='secret123')
        self.client.login(username='testuser', password='secret123')

    def tearDown(self):
        self.user.delete()

    # click create new account button
    def test_create_new_account_view(self):
        response = self.client.get(reverse("createaccount"))
        self.assertEqual(response.status_code, 200)

    # click on the home button
    def test_go_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    # click on the delete button
    def test_delete_account_view(self):
        response = self.client.get(reverse("accountbase"))
        self.assertEqual(response.status_code, 200)

    # click on the filter button
    def test_filter_account_view(self):
        response = self.client.get(reverse("accountbase"))
        self.assertEqual(response.status_code, 200)

    # click on the search button
    def test_search_account_view(self):
        response = self.client.get(reverse("accountbase"))
        self.assertEqual(response.status_code, 200)

    # click on the edit button
    def test_edit_account_view(self):
        id = self.user.id
        url = reverse("editaccount", kwargs={"id": id})
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
