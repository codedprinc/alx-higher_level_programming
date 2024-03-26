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
        self.check_if_integer(width, 'width')
        self.check_if_integer(height, 'height')
        self.check_if_integer(x, 'x')
        self.check_if_integer(y, 'y')

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
        self.check_if_integer(width, 'width')
        self.__width = width

    @property
    def height(self):
        """`int`: Returns the value of height"""
        return self.__height

    @height.setter
    def height(self, height):
        self.check_if_integer(height, 'height')
        self.__height = height

    @property
    def x(self):
        """`int`: Returns the value of x"""
        return self.__x

    @x.setter
    def x(self, x):
        self.check_if_integer(x, 'x')
        self.__x = x

    @property
    def y(self):
        """`int`: Returns the value of y"""
        return self.__y

    @y.setter
    def y(self, y):
        self.check_if_integer(y, 'y')
        self.__y = y


    def check_if_integer(self, value, param):
        """`any` check if `attr_i` is an `int`

        Raises:
          TypeError: If `attr_i` is not `int`.
        """
        if type(value) is not int:
            raise TypeError(param + ' must be an integer')

        if value <= 0 and param in ('width', 'height'):
            raise ValueError(param + ' must be > 0')

        if value < 0 and param in ('x', 'y'):
            raise ValueError(param + ' must be >= 0')
