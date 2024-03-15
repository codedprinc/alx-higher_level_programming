#!/usr/bin/python3
"""contains a class `Rectangle`"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Inherits properties from class `BaseGeometry`"""

    def __init__(self, width, height):
        """ initializes the class

        Args:
            width (int): The rectangle's width
            height (int): The rectangle's height
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
