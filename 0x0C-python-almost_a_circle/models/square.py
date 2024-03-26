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

    @property
    def size(self):
        """
        Getter for size value

        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the class `Square` by assigning an argument to each
        attribute.

        """

        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'size', 'x', 'y']

        if argc > 4:
            argc = 4

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)
