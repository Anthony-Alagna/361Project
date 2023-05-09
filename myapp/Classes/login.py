from django.shortcuts import redirect
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
                None,  # from_email
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


class ResetPassword():
    def __init__(self):
        pass

    def reset_password(self, token, new_password):
        """
        Resets the user's password.

        Args:
            token (str): The token used for password reset.
            new_password (str): The new password to be set.

        Returns:
            bool: True if the password was reset successfully, False otherwise.
        """

        if token is None or new_password is None or token == "" or new_password == "":
            raise ValueError("Token and new password must be provided")
        if ":" not in token:
            raise ValueError("Invalid token")

        try:
            # Split the token into the username and authentication string
            username, auth_str = token.split(":")

            # Retrieve the user from the database
            user = User.objects.get(email=username)

            # Check that the authentication string matches the one stored in the database
            if user.pw_reset_token.split(":")[1] == auth_str:
                # Update the user's password
                user.User_LogPass = new_password
                user.save()
                return True
            else:
                return False
        except Exception as e:
            raise e


class Logout:
    def __init__(self, request):
        if request.user.is_authenticated:
            del request.session['user_id']
            request.session.modified = True
        self.redirect = redirect('login')
