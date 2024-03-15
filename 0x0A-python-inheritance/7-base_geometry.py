#!/usr/bin/python3
"""Class `BaseGeometry`"""


class BaseGeometry:
    """has a function area"""

    def area(self):
        """
        Raises:
            Exception: area() is not implemented.
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validates `value`

        Args:
            name (str): a string
            value (int): an integer

        Raises:
           TypeError: if `value` is not an integer
           ValueError: if `value` is less or equal to `0`.

        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be '
                             'greater than 0'.format(name))
