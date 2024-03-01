#!/usr/bin/python3
"""Has a class rectangle"""


class Rectangle:
    """Defines a rectangle based on 7-rectangle.py

    Attributes:
        number_of_instances (int): counts the instances of initializations.
        print_symbol (chr): Holds the symbol to be printed
    """

    print_symbol = '#'
    number_of_instances = 0

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

        Rectangle.number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__height + self.__width)

    def __draw_rectangle(self):
        """

        Draw the Rectangle with their size

        Returns:
            str: `Empty` If width or height is `0`,
            otherwise returns a string with the Rectangle.

        """

        rect_str = ''
        w = self.__width
        h = self.__height

        if w == 0 or h == 0:
            return rect_str

        for i in range(h):
            for j in range(w):
                rect_str += str(self.print_symbol)

            if i != h - 1:
                rect_str += '\n'

        return rect_str

    def __str__(self):
        """
        Returns a string with the representation of the Rectangle.

        """
        return self.__draw_rectangle()

    def __repr__(self):
        """
        Returns the string representation of the rectangle
        """

        w = str(eval('self.width'))
        h = str(eval('self.height'))

        return 'Rectangle(' + w + ', ' + h + ')'

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted"""

        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares the biggest or equal area value between 2 rectangles

        Args:
          rect_1 (Rectangle); The first rectangle to compare
          rect_2 (Rectangle); The second rectangle to compare

        Returns:
          Rectangle: The Biggest Rectangle, or `rect_1` if the 2 rectangle
                      have the same area value.

        Raises:
          TypeError: If `rect1` or `rect_2` aren't an instance of the Rectangle
                    class.

        """

        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')

        rct1_area = rect_1.area()
        rct2_area = rect_2.area()

        if rct1_area >= rct2_area:
            return rect_1

        return rect_2
