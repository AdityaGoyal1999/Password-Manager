""" The main file to manage the passwords that the user has.
"""

from password_generator import Generator
from password_send_email import send_email


class Manager:
    """ This class manages the passwords that the person has.

    The master password is stored as dict["master"]

    === Attributes ===
    _passwords: stores the passwords of the user according to the
        website he is on.
    """
    _passwords: dict

    def __init__(self, master: str) -> None:
        """ Initializes the class.
        """
        self._passwords = {}
        self._passwords["master"] = master

    def enter_password(self, _id: str) -> None:
        """ Asks the user about the passord.

        Precondition: the choice will be in either True/ False.
        """
        choice = input(" Do you want to use a computer generated password?\n")
        if choice == "False":
            passw = input("Enter the password that you want to use.\n")
            self._passwords[_id] = passw
        elif choice == "True":
            _len = input("Enter the length of the password.\n")
            g = Generator(int(_len))
            passw = g.generate()
            self._passwords[id] = passw
            print(passw)
        else:
            raise PoorChoiceException

    def check_user(self, master) -> bool:
        """ Checks if the user is authentic or not.
        """
        if self._passwords['master'] == master:
            return True
        else:
            return False

    def get_password(self, master: str) -> str:
        """ Returns the password if the user is genuinely original.

        Enter the master password which should match else not password will be
        given
        """
        if self._passwords['master'] == master:
            which_password = input('Which password are you looking for?\n')
            return self._passwords[which_password]
        else:
            return "Invalid login"

    def change_password(self) -> None:
        """ Changes the stored password that the user has.
        """
        master = input("Enter the master key\n")
        if self.check_user(master):
            _id = input("Enter the id of the password to be changed.\n")
            new_password = input("Enter the new password.\n")
            if _id not in self._passwords:
                raise WrongChoiceException
            else:
                self._passwords[_id] = new_password
        else:
            print("Incorrect login.")

    def forgot_password(self) -> None:
        """ Sends a recovery email with the login information.
        """
        emailid = input("Enter you email id.\n")
        email_password = input("Enter the password.\n")
        send_email(emailid, email_password, self._passwords["master"])


class PoorChoiceException(Exception):
    """ The user doesn't know what to do.
    """

    def __str__(self):
        print('Really, are you serious!')


class WrongChoiceException(Exception):
    """ The user has made a wrong choice.
    """

    def __str__(self):
        print(" The input was invalid.")


if "__main__" == __name__:
    master_pass = input("Enter the master password\n")
    m = Manager(master_pass)
    m.enter_password('google')
