#!/usr/bin/python3
"""11. Student to disk and reload """


class Student:
    """
    my class student
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantates the class `Student`

        Args:
           first_name (str) : Student' s first name
           last_name (str) : Student' s last name.
           age (int) : Student' s age

        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        if `attrs`is a list of strings , only attribute names contained in this
        must be retrieved.

        """

        class_d = self.__dict__
        sel_d = dict()

        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return class_d

                if attr in class_d:
                    sel_d[attr] = class_d[attr]

            return sel_d
        return class_d

    def reload_from_json(self, json):
        """
        Replaces all attributes of the `Student` instance.

        - Assume `json` will always be a dictionary
        - A dictionary key will be the public attribute name
        - A dictionary value will be the value of the public attribute.

        """
        for i in json:
            if i in self.__dict__.keys():
                self.__dict__[i] = json[i]
