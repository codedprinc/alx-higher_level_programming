#!/usr/bin/python3
"""Module that has a function that adds 2 integers"""

def add_integer(a, b=98):
    """adds two integers
    Args:
       a (:obj:`int, float`): first number.
       b (:obj:`int, float`, optional): second number.

    Returns:
       int: addition of `a` and `b`.

    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('a must be an integer')

    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b = int(b)

    return a + b

if __name__ == "__main__":
    print(add_integer('b', 23))
