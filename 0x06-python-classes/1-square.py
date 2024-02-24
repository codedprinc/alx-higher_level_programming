#!/usr/bin/python3
"""This module defines a  Square class

Classes:
  Square: Represents a square with a private instance attribute 'size'.

Example:
  >>> square_instance = Square(19)

"""


class Square:
    """
    Represents a square

    Attributes:
    - __size (int): The size of a square

    Methods:
    - __init__(size): Initializes the size value of the a new Square instance

    """

    def __init__(self, size):
        """__init__

        The __init__ method initializes the size value
        of the square.

        Attributes:
            size (int): The size of the square.

        """
        self.__size = size
