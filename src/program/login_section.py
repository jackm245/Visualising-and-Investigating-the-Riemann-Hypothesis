"""
login_section.py
================

Contains all of the classes used to interact with the GUI for the
Login section of the project

Includes the Login, Sign Up, Forgotten Password, and Reset Password Screens
"""

import re
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from .user_interface import Ui_LoginScreen, Ui_SignUpScreen, Ui_ForgottenPasswordScreen, Ui_ForgottenPassword2Screen, Ui_ResetPasswordScreen, Ui_ResetPassword2Screen
from .utils import database_insert, database_select, database_query, database_print, hash_password, check_password, send_verification_email, User, Screen


class LoginSection(Screen):

    """
    A class inherited by all of the Screens/Page classes in the login section
    of the program

    The functions defined in this class allow for different pages to be loaded
    and hidden, so that the user is able to navigate to different parts of the
    login section using the GUI

    It also contains some functions which are commonly used in many of the
    Classes that inherit this class
    """

    def __init__(self):
        super(LoginSection, self).__init__()

    def goto_login(self):
        self.login = Login()
        self.hide()

    def goto_signup(self):
        self.signup = SignUp()
        self.hide()

    def goto_forgotten_password(self):
        self.forgotten_password = ForgottenPassword()
        self.hide()

    def goto_reset_password(self):
        self.reset_password = ResetPassword()
        self.hide()

    def are_invalid_passwords(self):

        """
        Inputs: self.password1: string, self.password2: string
        Outputs: strings or bool

        Checks to see if the input passwords are invalid

        If both of the input password are the same and meet the following criteria:
             - At least one uppercase letter
             - At least one lowercase letter
             - At least one digit
             - At least 8 characters long
        Then the bool value False is Output

        Otherwise, the passwords do not meet the criteria, so a string is output
        describing why they do not meet the criteria. This string has the bool
        value True
        """

        if not re.fullmatch('(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9]).{8,}', self.password1):
            return "Password must contain lower case, upper case,\na number, and be at least 8 characters long"
        elif self.password1 != self.password2:
            return "Passwords do not match"
        else:
            return False


class ResetPassword2(LoginSection):

    """
    Displays the Second Screen in the Reset Password part of the Login Section

    This is the screen where the user is actually able to permenantly change
    their password
    """

    def __init__(self):
        super(ResetPassword2, self).__init__()
        self.ui = Ui_ResetPassword2Screen()
        self.ui.setupUi(self)
        self.ui.SubmitButton.clicked.connect(self.submit)
        self.show()

    def submit(self):
        self.password1 = self.ui.PasswordInput.text()
        self.password2 = self.ui.ConfirmPasswordInput.text()
        self.pwds_invalid = self.are_invalid_passwords()
        if self.pwds_invalid:
            self.ui.ErrorLabel.setText(self.pwds_invalid)
        else:
            database_query("UPDATE Users SET Password=? WHERE User_ID=?",(hash_password(self.password1), User.GetUserID(),))
            from .main_section import MainMenu
            self.main_menu = MainMenu()
            self.hide()


class ResetPassword(LoginSection):

    """
    Displays the first screen in the Reset Password part of the Login Section

    On this screen, the user is required to login to confirm that the user is
    actually the person who owns the account
    """

    def __init__(self):
        super(ResetPassword, self).__init__()
        self.ui = Ui_ResetPasswordScreen()
        self.ui.setupUi(self)
        self.show_or_hide = 'Show'
        self.ui.LoginTab.clicked.connect(self.goto_login)
        self.ui.SignUpTab.clicked.connect(self.goto_signup)
        self.ui.ForgottenPasswordTab.clicked.connect(self.goto_forgotten_password)
        self.ui.ShowHideButton.clicked.connect(self.show_hide)
        self.ui.SubmitButton.clicked.connect(self.submit)
        self.show()

    def show_hide(self):
        if self.show_or_hide == 'Show':
            self.ui.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.show_or_hide = 'Hide'
        else:
            self.ui.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
            self.show_or_hide = 'Show'
        self.ui.ShowHideButton.setText(self.show_or_hide)

    def submit(self):
        self.username = self.ui.UsernameInput.text()
        self.password  = self.ui.PasswordInput.text()
        self.selection = database_select(['User_ID', 'Username'], ['Users'])
        self.id1 = [row[0] for row in self.selection if row[1] == self.username]
        self.selection = database_select(['User_ID', 'Password'], ['Users'])
        self.id2 = [row[0] for row in self.selection if check_password(self.password, row[1])]
        if len(self.id1) == 0 or self.id1 != self.id2:
            self.ui.ErrorLabel.setText("Username or password is not valid")
        else:
            User.SetSignedIn(True)
            User.SetUsername(self.username)
            User.SetUserID(self.id1[0])
            self.email = database_query("SELECT Email FROM Users WHERE User_ID=?", (self.id1[0],))[0][0]
            User.SetEmail(self.email)
            self.reset_password_2 = ResetPassword2()
            self.hide()


class ForgottenPassword2(LoginSection):

    """
    Displays the second screen in the Forgotten Password part of the Login Section

    This is the screen where the user enter's the verification code that they
    have been emailed to confirm that they are the owners of that account

    The user will then be immediately taken to the ResetPassword screen, once
    they submit the correct verification code
    """

    def __init__(self, verification_code):
        super(ForgottenPassword2, self).__init__()
        self.verification_code = verification_code
        self.ui = Ui_ForgottenPassword2Screen()
        self.ui.setupUi(self)
        self.ui.LoginTab.clicked.connect(self.goto_login)
        self.ui.SignUpTab.clicked.connect(self.goto_signup)
        self.ui.ResetPasswordTab.clicked.connect(self.goto_reset_password)
        self.ui.SubmitButton.clicked.connect(self.submit)
        self.show()

    def submit(self):
        # Check verification code
        self.user_input = self.ui.VerificationCodeInput.text()
        if self.user_input == self.verification_code:
            User.SetSignedIn(True)
            self.reset_password_2 = ResetPassword2()
            self.hide()
        else:
            self.ui.ErrorLabel.setText("Verification Code Incorrect")


class ForgottenPassword(LoginSection):

    """
    Displays the first screen in the Forgotten Password part of the Login Section

    This is the screen where the user is asked to enter the email associated
    with their account. An email is then sent to the user containing a
    6 digit pseudorandom security code that they will tehn have to enter on the
    following screen
    """

    def __init__(self):
        super(ForgottenPassword, self).__init__()
        self.ui = Ui_ForgottenPasswordScreen()
        self.ui.setupUi(self)
        self.ui.LoginTab.clicked.connect(self.goto_login)
        self.ui.SignUpTab.clicked.connect(self.goto_signup)
        self.ui.ResetPasswordTab.clicked.connect(self.goto_reset_password)
        self.ui.SubmitButton.clicked.connect(self.submit)
        self.show()

    def submit(self):
        self.email  = self.ui.EmailInput.text()
        self.selection = database_query("SELECT Email FROM Users WHERE Email=?", (self.email,))
        if len(self.selection) == 0:
            self.ui.ErrorLabel.setText("Email is not registered")
        else:
            # Send Email
            self.verificaton_code = ''.join(list(map(str, [random.randint(0, 9) for _ in range(6)])))
            self.user_id = database_query("SELECT User_ID FROM Users WHERE Email=?", (self.email,))[0][0]
            self.username = database_query("SELECT Username FROM Users WHERE Email=?", (self.email,))[0][0]
            User.SetUserID(self.user_id)
            User.SetUsername(self.username)
            User.SetEmail(self.email)
            send_verification_email(self.verificaton_code)
            self.forgotten_password_2 = ForgottenPassword2(self.verificaton_code)
            self.hide()


class SignUp(LoginSection):

    """
    Displays Sign Up screen as part of the Login Section

    This is the screen where the user is able to create an account
    They enter their username, email, and password (twice). Given that this data
    is all valid, the data is stored to the database, and the user's account
    has been permenantly created.
    """

    def __init__(self):
        super(SignUp, self).__init__()
        self.ui = Ui_SignUpScreen()
        self.ui.setupUi(self)
        self.show_or_hide = 'Show'
        self.show_or_hide_2 = 'Show'
        self.ui.LoginTab.clicked.connect(self.goto_login)
        self.ui.ForgottenPasswordTab.clicked.connect(self.goto_forgotten_password)
        self.ui.ResetPasswordTab.clicked.connect(self.goto_reset_password)
        self.ui.ShowHideButton.clicked.connect(self.show_hide)
        self.ui.ShowHideButton_2.clicked.connect(self.show_hide_2)
        self.ui.SubmitButton.clicked.connect(self.submit)
        self.show()

    def show_hide(self):
        if self.show_or_hide == 'Show':
            self.ui.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.show_or_hide = 'Hide'
        else:
            self.ui.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
            self.show_or_hide = 'Show'
        self.ui.ShowHideButton.setText(self.show_or_hide)

    def show_hide_2(self):
        if self.show_or_hide_2 == 'Show':
            self.ui.PasswordInput_2.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.show_or_hide_2 = 'Hide'
        else:
            self.ui.PasswordInput_2.setEchoMode(QtWidgets.QLineEdit.Password)
            self.show_or_hide_2 = 'Show'
        self.ui.ShowHideButton_2.setText(self.show_or_hide_2)

    def submit(self):
        from .main_section import MainMenu
        self.username = self.ui.UsernameInput.text()
        self.email = self.ui.EmailInput.text()
        self.password1  = self.ui.PasswordInput.text()
        self.password2  = self.ui.PasswordInput_2.text()
        self.pwds_invalid = self.are_invalid_passwords()
        # check is of right form
        if not re.fullmatch('\w{1,20}', self.username):
            self.ui.ErrorLabel.setText("Username must be at 1-20 characters long\nand not contain special characters")
        elif not re.fullmatch('.+@.+\..+', self.email):
            self.ui.ErrorLabel.setText("Email address must be valid")
        elif self.pwds_invalid:
            self.ui.ErrorLabel.setText(self.pwds_invalid)
        else:
            self.selection = database_select(['Username'], ['Users'])
            self.Usernames = set([row[0] for row in self.selection])
            if self.username in self.Usernames:
                self.ui.ErrorLabel.setText("Username already taken")
            else:
                self.selection = database_select(['Email'], ['Users'])
                self.Emails = set([row[0] for row in self.selection])
                if self.email in self.Emails:
                    self.ui.ErrorLabel.setText("Email already taken")
                else:
                    self.selection = database_select(['User_ID'], ['Users'])
                    self.User_IDs = set([row[0] for row in self.selection])
                    self.User_ID = self.get_user_id()
                    self.hashed_password = hash_password(self.password1)
                    database_insert('Users', [self.User_ID, self.username, self.email, self.hashed_password])
                    User.SetSignedIn(True)
                    User.SetUserID(self.User_ID)
                    User.SetUsername(self.username)
                    User.SetEmail(self.email)
                    self.main_menu = MainMenu()
                    self.hide()

    def get_user_id(self, User_ID=0):
        if User_ID not in self.User_IDs:
            return User_ID
        else:
            return self.get_user_id(User_ID+1)


class Login(LoginSection):

    """
    Displays Login screen as part of the Login Section
    This screen is the main entry point to the login section

    The user can use this screen to sign in to an account that they have
    previously created
    """

    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
        self.ui.SignUpTab.clicked.connect(self.goto_signup)
        self.ui.ForgottenPasswordTab.clicked.connect(self.goto_forgotten_password)
        self.ui.ResetPasswordTab.clicked.connect(self.goto_reset_password)
        self.ui.BackButton.clicked.connect(self.goto_mainmenu)
        self.ui.SubmitButton.clicked.connect(self.submit)
        self.ui.ShowHideButton.clicked.connect(self.show_hide)
        self.show_or_hide = 'Show'
        self.show()

    def submit(self):
        from .main_section import MainMenu
        self.username = self.ui.UsernameInput.text()
        self.password  = self.ui.PasswordInput.text()
        self.selection = database_select(['User_ID', 'Username'], ['Users'])
        self.id1 = [row[0] for row in self.selection if row[1] == self.username]
        self.selection = database_select(['User_ID', 'Password'], ['Users'])
        self.id2 = [row[0] for row in self.selection if check_password(self.password, row[1])]
        if len(self.id1) == 0 or self.id1 != self.id2:
            self.ui.ErrorLabel.setText("Username or password is not valid")
        else:
            User.SetSignedIn(True)
            User.SetUsername(self.username)
            User.SetUserID(self.id1[0])
            self.email = database_query("SELECT Email FROM Users WHERE User_ID=?", (self.id1[0],))[0][0]
            User.SetEmail(self.email)
            self.main_menu = MainMenu()
            self.hide()

    def show_hide(self):
        if self.show_or_hide == 'Show':
            self.ui.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.show_or_hide = 'Hide'
        else:
            self.ui.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
            self.show_or_hide = 'Show'
        self.ui.ShowHideButton.setText(self.show_or_hide)
