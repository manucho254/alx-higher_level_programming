#!/usr/bin/python3

""" Class Student
"""


class Student:
    """ defines class Student
    """
    def __init__(self, first_name, last_name, age):
        """ initialize class Student
            Args:
                 first_name: the fistname of a student
                 last_name: the lastname of a student
                 age: the age of a student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieve a dictionary representation of a Student
        """
        return self.__dict__
