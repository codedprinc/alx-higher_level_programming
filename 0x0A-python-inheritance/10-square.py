#!/usr/bin/python3
""" Contains a class `square`

"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """ Sqaure that inherits properties from class `Rectangle`"""

    def __init__(self, size):
        """
        Args:
            size (int): the size of the square

        """

        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """ """
        return (self.__size ** self.__size)
