#!/usr/bin/python3
"""
This module contains the class `square`
and it s methods
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    The class `Square`
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for this class

        Args:
           size (int): Size of the square.
           x (int): Points of the square.
           y (int): Points of the square
        """

        super().__init__(size, size, x, y, id)


    def __str__(self):
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.\
            format(self.id, self.x, self.y, self.height)
