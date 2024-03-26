#!/usr/bin/python3
"""
1. Base Class

Module contains answer to task 1

"""


class Base:
    """
    My class `Base`

    Manage `id` attribute in all future classes and to avoid
      duplicating the same code (by extension, same bugs).

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instatates the class

        Args:
           id (int): if it is not `None` , assign the public instance attribute
                   `id` with this argument value . Otherwise , increment \
        `__nb_objects` and assign the new value to `id`.

        """

        self.id = id

        if self.id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
