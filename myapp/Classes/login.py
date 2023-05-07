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

    def send_reset_email(self, username, message=None, subject=None):
        """
        Sends a password reset email to the specified user.

        Args:
            username (str): The username or email address of the user.
            message (str, optional): The custom message to include in the email.
                If not provided, a default message with a password reset link will be generated.

        Returns:
            bool: True if the email was sent successfully, False otherwise.

        Raises:
            Exception: If an error occurs while sending the email.

        """

        if message is None:
            token = self._generate_token(username)
            # Generate the message to be sent to the user if one was not provided
            message = self._generate_message(token)
            subject = "Password Reset"

        try:
            send_mail(
                subject,  # subject
                message,  # message
                self.email,  # from_email
                [username],  # recipient_list
                fail_silently=False,
            )
            return True
        except Exception as e:
            raise e

    def _generate_token(self, username):
        """
        Generates a token to be used for password reset.

        Args:
            username (str): The username or email address of the user.

        Returns:
            str: The generated token string.
        """

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

    def _generate_message(self, token):
        """
        Generates a message for password reset email.

        Args:
            token (str): The token used for password reset.

        Returns:
            str: The generated message with a password reset link.
        """
        callback_url = f"http://tascheduler.aalagna.com/reset_password?token={token}"
        message = f"Please click the link below to reset your password:\n\n{callback_url}"
        return message
