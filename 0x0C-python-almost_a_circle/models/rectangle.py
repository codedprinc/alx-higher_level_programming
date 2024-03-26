#!/usr/bin/python3
"""
2. First Rectangle

Answer to the second task

"""

from models.base import Base


class Rectangle(Base):
    """
    It inherits it s properties from the class `Base`.

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        It intializes the class `Rectangle`

        Args:
           width (int): Width of the rectangle
           height (int): height of the rectangle
           x (int): a coordinate or position of a point
           y (int): a coordinate or position of a point

        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """`int`: Returns the value of width"""
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        """`int`: Returns the value of height"""
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        """`int`: Returns the value of x"""
        return self.__x

    @x.setter
    def x(self, width):
        self.__x = x

    @property
    def y(self):
        """`int`: Returns the value of y"""
        return self.__y

    @y.setter
    def y(self, width):
        self.__y = y
