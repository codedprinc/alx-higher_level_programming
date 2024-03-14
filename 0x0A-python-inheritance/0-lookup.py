#!/usr/bin/python3
"""0.Lookup

Module contains a function that returns the list of available attributes and
methods of an object.

"""


def lookup(obj):
    """Returns a list of avaialble attributes and methods of an object

    Args:
       (obj) : the object to be scanned.

    Returns:
        `list` object.
    """

    return dir(obj)
