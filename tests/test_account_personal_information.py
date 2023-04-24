import unittest

from myapp.Classes import users
from myapp.models import User


class PersonalInformationTest(unittest.TestCase):

    def setUp(self):
        self.user1 = User.objects.create(
            User_LogName="testUser1",
            User_LogPass="testPass1",
            User_Email="testuser1@test.com",
            User_fName="Bob",
            User_lName="Smith",
            User_Phone="1111111111",
            User_Address="123 Blvd",
            User_Pos="TA"
        )

        self.user2 = User.objects.create(
            User_LogName="testUser2",
            User_LogPass="testPass2",
            User_Email="test@test.com",
            User_fName="John",
            User_lName="Doe",
            User_Phone="2222222222",
            User_Address="456 St",
            User_Pos="IN"
        )

    def test_get_account_info(self):
        self.assertEqual("test@gmail.com", users.getAccountInfo(self.user1.username), "Should return email of "
                                                                                      "account")

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
