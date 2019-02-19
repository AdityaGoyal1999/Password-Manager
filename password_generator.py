""" This is the starter file for the password geenrator.
"""
import random


class Generator:
    """ This class generates the password for the user.

    === Attributes ===
    _length: the length of the password
    """
    _length: int

    def __init__(self, length: int) -> None:
        """ The length of the password string.
        """
        self._length = length

    def getLength(self) -> int:
        """ Returns the length of the password.
        """
        return self._length

    def generate(self) -> str:
        """ Generates the random password for the user which is hard to guess.
        """
        output = ""
        for _ in range(self._length):
            temp = chr(random.randint(48, 122))
            output += temp
        return output


if '__main__' == __name__:

    g = Generator(7)
    print(g.generate())
