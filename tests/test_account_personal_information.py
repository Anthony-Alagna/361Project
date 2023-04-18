import unittest
from django.test import TestCase, Client
from myapp.models import User
from unittest.mock import Mock


class MyTestCase(unittest.TestCase):
    def setUp(self):
        user = Mock()
        user.email = "test@gmail.com"
        user.email = "test@gmail.com"
        user.username = "testUsername"
        user.phone = "1111111111"
        user.address = "123 Blvd"
        user.fName = "Bob"
        user.lName = "Smith"
    def test_get_account_info(self):
        self.assertEqual("test@gmail.com", self.getAccountInfo(self.username))

    def test_edit_account_info(self):
        self.setUp
        self.assertEqual(user.email, "test@gmail.com")


if __name__ == '__main__':
    unittest.main()
