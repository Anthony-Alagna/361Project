import random
import string
from myapp.models import User
from django.core.mail import send_mail


class ForgotPassword:
    """
    Class for handling password reset functionality.
    """

    def __init__(self):
        pass

    """_summary_ : sends the user an email to reset their password
        _params_ : username - The username of the account that needs to reset their password
                     message - The message to be sent to the user (optional)
        _returns_ : True if the email was sent successfully, otherwise raises an error
    """

    def send_reset_email(self, username, message=None):

        if message is None:
            token = self._generate_token(username)
            # Generate the message to be sent to the user if one was not provided
            message = self._generate_message(
                "Password Reset", f"Please click the link below to reset your password:\n\n{token}"
            )

        try:
            send_mail(
                "Password Reset",  # subject
                message,  # message
                self.email,  # from_email
                [username],  # recipient_list
                fail_silently=False,
            )
            return True
        except Exception as e:
            raise e

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
