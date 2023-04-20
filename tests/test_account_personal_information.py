import unittest

from myapp.Classes import users


class PersonalInformationTest(unittest.TestCase):
    def setUp(self):
        self.user1 = users()
        self.user1.email = "test@gmail.com"
        self.user1.username = "testUsername"
        self.user1.phone = "1111111111"
        self.user1.address = "123 Blvd"
        self.user1.fName = "Bob"
        self.user1.lName = "Smith"
        self.user1.position = "TA"

        self.user2 = users()
        self.user2.email = ""
        self.user2.username = "testUser2"
        self.user2.phone = "2222222222"
        self.user2.address = "234 Rd"
        self.user2.fName = "John"
        self.user2.lName = "Smith"
        self.user2.position = "TA"

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
        self.user1.editInfo(self.user1.phone, self.user1.address, "Joe", self.user1.position)
        self.assertEqual(self.user1.email, "test@gmail.com", "email should not have changed")
        self.assertEqual(self.user1.phone, "1111111111", "Phone number should not have changed")
        self.assertEqual(self.user1.fName, "Joe", "First name should have changed")
        self.assertEqual(self.user1.lName, "Smith", "Last name should not have changed")
        self.assertEqual(self.user1.address, "123 Blvd", "Address should not have changed")
        self.assertEqual(self.user1.position, "TA", "Position should not have changed")

    def test_edit_account_info_change_phone(self):
        # Change the phone number
        self.user1.editInfo("3333333333", self.user1.address, self.user1.fName, self.user1.position)
        self.assertEqual(self.user1.email, "test@gmail.com", "email should not have changed")
        self.assertEqual(self.user1.phone, "3333333333", "Phone number should have changed")
        self.assertEqual(self.user1.fName, "Bob", "First name should not have changed")
        self.assertEqual(self.user1.lName, "Smith", "Last name should not have changed")
        self.assertEqual(self.user1.address, "123 Blvd", "Address should not have changed")
        self.assertEqual(self.user1.position, "TA", "Position should not have changed")

    def test_edit_account_info_change_address(self):
        # Change the address
        self.user1.editInfo(self.user1.phone, "789 Blvd", self.user1.fName, self.user1.position)
        self.assertEqual(self.user1.email, "test@gmail.com", "email should not have changed")
        self.assertEqual(self.user1.phone, "1111111111", "Phone number should not have changed")
        self.assertEqual(self.user1.fName, "Bob", "First name should not have changed")
        self.assertEqual(self.user1.lName, "Smith", "Last name should not have changed")
        self.assertEqual(self.user1.address, "789 Blvd", "Address should have changed")
        self.assertEqual(self.user1.position, "TA", "Position should not have changed")

    def test_edit_account_info_change_position(self):
        # Change the position
        self.user1.editInfo(self.user1.phone, self.user1.address, self.user1.fName, "Professor")
        self.assertEqual(self.user1.email, "test@gmail.com", "email should not have changed")
        self.assertEqual(self.user1.phone, "1111111111", "Phone number should not have changed")
        self.assertEqual(self.user1.fName, "Bob", "First name should not have changed")
        self.assertEqual(self.user1.lName, "Smith", "Last name should not have changed")
        self.assertEqual(self.user1.address, "123 Blvd", "Address should not have changed")
        self.assertEqual(self.user1.position, "Professor", "Position should have changed")