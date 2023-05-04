from myapp.models import User, Course, Section, CourseToUser
import smtplib

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
    """

    def send_reset_email(self, username):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.email, self.password)
            message = f"Subject: Password reset for {username}\n\nPlease click on the following link to reset your password: http://example.com/reset/{username}"
            server.sendmail(self.email, username, message)
            server.quit()
            print("Password reset email sent successfully!")
        except:
            print("Sorry, something went wrong. Please try again later.")
