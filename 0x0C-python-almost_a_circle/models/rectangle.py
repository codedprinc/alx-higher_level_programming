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

    def area(self):
        """ area of the rectangle"""

        return self.__width * self.__height

    def display(self):
        """ prints in stdout the `Rectangle` instance with
           the character `#`.


        h = self.__height
        w = self.__width

        for i in range(0, h):
            for j in range(0, w):
                print("#", end="")
            print()

        """
        if self.__y > 0:
            print('\n' * self.__y, end='')

        for i in range(self.height):
            if self.__x > 0:
                print(' ' * self.__x, end='')

            print('#' * self.__width)

    def __str__(self):
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".\
            format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Updates the class `Rectangle` by assigning an argument to each
        attribute.

        ## This was when only having args as the parameter; no kwargs.

        list_1 = []
        list_names = ['id', 'width', 'height', 'x', 'y']
        for arg in args:
            list_1.append(arg)

        arg_len = len(args)

        if arg_len > 0:
            for i in range(0, arg_len:
                setattr(self, list_names[i], list_1[i])

        """

        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'width', 'height', 'x', 'y']

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                settattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)
