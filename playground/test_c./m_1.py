#!/usr/bin/python3
"""Tesing module"""

def my_function(a, b):
    """
    >>> my_function(2, 3)
    6
    >>> my_function('v', 2)
    'vv'
    """
    return a * b

class MyClass:
    """Test on how ellipsis for doctests with unpredictable ways"""
    pass

def unpredictable(obj):
    """Returns a new list containing obj.
    
    >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
    [<m_1.MyClass object at 0x...>]
    """
    return [obj]
