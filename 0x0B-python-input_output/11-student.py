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

    def to_json(self, attrs=None):
        """ Retrieve a dictionary representation of a Student
            Args:
                attrs: names of attributes
            Return:
                  a dictionary representation of a Student
        """
        data = self.__dict__
        if attrs is not None:
            return dict({x: y for x, y in data.items() if x in attrs})
        return data

    def reload_from_json(self, json: dict):
        """ replace all attributes of student instance
            Args:
                json: json data
        """
        self.first_name = json.get("first_name")
        self.last_name = json.get("last_name")
        self.age = json.get("age")
