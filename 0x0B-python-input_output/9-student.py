#!/usr/bin/python3
""" 9. Student to JSON """


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

        def to_json(self):
            """
            retrieves a dictionary representation of a Student instance
            """

            return self.__dict__
