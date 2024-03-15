#!/usr/bin/python3
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

    def area(self):
        """Performs the area of the rectangle"""

        return (self.__width * self.__height)

    def __str__(self):
        """
        Returns:
            [Rectangle] <width>/<height>
        """

        return "[Rectangle] {}/{}".format\
            (str(self.__width), str(self.__height))
