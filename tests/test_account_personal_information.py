import unittest
from django.test import TestCase, Client
from myapp.models import User


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.email = "test@gmail.com"
        self.username = "testUsername"

    def test_get_account_info(self):
        self.assertEqual("test@gmail.com", self.getAccountInfo(self.username))


if __name__ == '__main__':
    unittest.main()
