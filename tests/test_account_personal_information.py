import unittest

from myapp.Classes.users import Users
from myapp.models import User


class PersonalInformationTest(unittest.TestCase):

    def setUp(self):
        self.user1 = User.objects.create(User_fName='tester', User_lName="Smith",
                                         User_Email='user1@example.com',
                                         User_Pos='TA', User_Phone='1234567890',
                                         User_Address='123 Main St', User_City="Milwaukee",
                                         User_LogName='user1ish', User_LogPass='password14',
                                         User_begin='2022-01-01 00:00:00', User_Updated='2023-04-18 00:00:00'
                                         )

    def tearDown(self):
        self.user1.delete()

    def test_get_account_info(self):
        resp = Users.getAccountInfo(
            self.user1.User_LogName, self.user1.id)
        self.assertEqual(resp[0], "tester", "First name should be Bob")
        self.assertEqual(resp[1], "Smith", "Last name should be Smith")
        self.assertEqual(resp[2], "user1ish",
                         "Usernamelogname should be user1")
        self.assertEqual(
            resp[3], "user1@example.com" "Email should be test@test.com")
        self.assertEqual(resp[4], "TA", "Position should be TA")

    def test_get_account_info_unknown_account(self):
        # Should raise an exception if the account doesn't exist
        with self.assertRaises(LookupError, "Should raise exception if account doesn't exist"):
            users.getAccountInfo("fakeusername")

    def test_get_account_info_no_email(self):
        self.assertEqual("", users.getAccountInfo(self.user2.username), "Should return an empty string if email"
                                                                        "doesn't exist for user")

    def test_edit_account_info_change_fName(self):
        # Change the firstName
        self.user1.editInfo(
            self.user1.phone, self.user1.address, "Joe", self.user1.position)
        self.assertEqual(self.user1.email, "test@gmail.com",
                         "email should not have changed")
        self.assertEqual(self.user1.phone, "1111111111",
                         "Phone number should not have changed")
        self.assertEqual(self.user1.fName, "Joe",
                         "First name should have changed")
        self.assertEqual(self.user1.lName, "Smith",
                         "Last name should not have changed")
        self.assertEqual(self.user1.address, "123 Blvd",
                         "Address should not have changed")
        self.assertEqual(self.user1.position, "TA",
                         "Position should not have changed")

    def test_edit_account_info_change_phone(self):
        # Change the phone number
        self.user1.editInfo("3333333333", self.user1.address,
                            self.user1.fName, self.user1.position)
        self.assertEqual(self.user1.email, "test@gmail.com",
                         "email should not have changed")
        self.assertEqual(self.user1.phone, "3333333333",
                         "Phone number should have changed")
        self.assertEqual(self.user1.fName, "Bob",
                         "First name should not have changed")
        self.assertEqual(self.user1.lName, "Smith",
                         "Last name should not have changed")
        self.assertEqual(self.user1.address, "123 Blvd",
                         "Address should not have changed")
        self.assertEqual(self.user1.position, "TA",
                         "Position should not have changed")

    def test_edit_account_info_change_address(self):
        # Change the address
        self.user1.editInfo(self.user1.phone, "789 Blvd",
                            self.user1.fName, self.user1.position)
        self.assertEqual(self.user1.email, "test@gmail.com",
                         "email should not have changed")
        self.assertEqual(self.user1.phone, "1111111111",
                         "Phone number should not have changed")
        self.assertEqual(self.user1.fName, "Bob",
                         "First name should not have changed")
        self.assertEqual(self.user1.lName, "Smith",
                         "Last name should not have changed")
        self.assertEqual(self.user1.address, "789 Blvd",
                         "Address should have changed")
        self.assertEqual(self.user1.position, "TA",
                         "Position should not have changed")

    def test_edit_account_info_change_position(self):
        # Change the position
        self.user1.editInfo(self.user1.phone, self.user1.address,
                            self.user1.fName, "Professor")
        self.assertEqual(self.user1.email, "test@gmail.com",
                         "email should not have changed")
        self.assertEqual(self.user1.phone, "1111111111",
                         "Phone number should not have changed")
        self.assertEqual(self.user1.fName, "Bob",
                         "First name should not have changed")
        self.assertEqual(self.user1.lName, "Smith",
                         "Last name should not have changed")
        self.assertEqual(self.user1.address, "123 Blvd",
                         "Address should not have changed")
        self.assertEqual(self.user1.position, "Professor",
                         "Position should have changed")
