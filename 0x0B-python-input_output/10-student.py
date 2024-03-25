#!/usr/bin/python3
"""10. Student to JSON with filter """


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
