""" The main file to manage the passwords that the user has.
"""

from password_generator import Generator
from typing import Optional


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


class PoorChoiceException(Exception):
    """ The user doesn't know what to do.
    """

    def __str__(self):
        print('Really, are you serious!')


if "__main__" == __name__:
    master_pass = input("Enter the master password\n")
    m = Manager(master_pass)
    m.enter_password('google')
