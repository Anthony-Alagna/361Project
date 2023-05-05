import random
import ssl
import string
from myapp.models import User, Course, Section, CourseToUser
import smtplib
import os

# this class implements methods to send the user
# an email to reset their password if they forgot it


class ForgotPassword:

    """
    _summary_ : constructor for the ForgotPassword class
    _params_ : email - The email of the account being used to send the pass reset email
                password - The password of the account being used to send the pass reset email
    """

    def __init__(self, email, password):
        self.email = email
        self.password = password

    """_summary_ : sends the user an email to reset their password
        _params_ : username - The username of the account that needs to reset their password
        _returns_ : True if the email was sent successfully, otherwise raises an error
    """

    def send_reset_email(self, username, message=None):
        # create a secure ssl context
        context = ssl.create_default_context()

        if message is None:
            token = self._generate_token(username)
            # Generate the message to be sent to the user if one was not provided
            message = self._generate_message(
                "Password Reset", f"Please click the link below to reset your password:\n\n{token}")

        # Send the email to the user
        try:
            server = smtplib.SMTP(os.getenv("MAIL_SERVER"), 587)
            server.starttls(context=context)
            server.login(self.email, self.password)
            server.sendmail(self.email, username, message)
            return True
        except Exception as e:
            print(e)
        finally:
            server.quit()

        """
        _summary_ : generates a token for the user to reset their password
        _params_ : username - The username of the account that needs to reset their password
        """

    def _generate_token(self, username):
        # Generate a random string of 20 characters for the authentication portion of the token
        auth_str = ''.join(random.choices(
            string.ascii_uppercase + string.ascii_lowercase + string.digits, k=20))
        # Combine the username and authentication string to create the token
        token = f"{username}:{auth_str}"

        # Store the token in the database
        user = User.objects.get(email=username)
        user.pw_reset_token = token
        user.save()
        return token

    def _generate_message(self, subject, body):
        # Generate the message to be sent to the user
        message = f"Subject: {subject}\n\n{body}"
        return message
