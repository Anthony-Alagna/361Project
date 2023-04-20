from django.test import TestCase, Client
from myapp.models import User

"""_summary_ contains unit tests for the login page
    """


class LoginTest(TestCase):

    def setUp(self):
        self.client = Client()
        for i in range(10):
            User.objects.create(
                User_LogName=(i),
                User_LogPass=str(i),
            )
<<<<<<< HEAD
=======

    def test_login_accessible(self):
        """_summary_ tests that the login page is accessible
        """
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
>>>>>>> origin/main
