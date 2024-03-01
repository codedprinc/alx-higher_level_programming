#!/usr/bin/python3
"""Has a class rectangle"""


class Rectangle:
    """Defines a rectangle based on 1-rectangle.py"""

    def __init__(self, width=0, height=0):
        """Initializes the class with two arguments

        Args:
          width (:obj:`int`, optional): Rectangle' s width.
          height (:obj:`int`, optional): Rectangle ' s height.

        Raises:
           TypeError: If `width` or `height` type is not `int`

           ValueError: If `width` or `height` type is less than `0`

        """

        if type(width) is not int:
            raise TypeError('width must be an integer')

        if width < 0:
            raise ValueError('width must be >= 0')

        if type(height) is not int:
            raise TypeError('height must be an integer')

        if height < 0:
            raise ValueError('height must be >= 0')

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """int: retireves the value of width"""

        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """int: retireves the value of height"""

        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return 2 * (self.__height + self.__width)
