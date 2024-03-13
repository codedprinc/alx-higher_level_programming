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

def main():
    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3
        def my_meth(self):
            pass

    print(lookup(MyClass1))

main()
