#!/usr/bin/python3
"""
1. Base Class

Module contains answer to task 1

"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representaion of list_diciotnaries.

        Args:
           list_dictionaries (`list` of `dict`): List of dicitionaries.
            If `list_dictionaries` is `None` or empty, return `[]`
                otherwise, return the JSON string representation of
            list_dictionaries.

        Returns:
           `JSON` string representaion of list_dictionaries.

        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of `list_objs` to a file

        """
        filename = cls.__name__ + '.json'

        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string([]))
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))

#            json_attrs = []

#            for elem in list_objs:
 #               json_attrs.append(elem.to_dictionary())

  #          return f.write(cls.to_json_string(json_attrs))
