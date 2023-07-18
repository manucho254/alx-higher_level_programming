#!/usr/bin/python3
""" Base class
"""
import json


class Base():
    """ base class for all other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize the base class
            Args:
                id: integer value
        """

        if id is None:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ convert list of dictionaries to Json.
            Args:
                list_dictionaries: list of dictionaries.
            Return:
                  Json string representation.
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ write Json string representation to file
        """

        arr = []

        if list_objs is None:
            with open("Rectangle.json", "w") as my_file:
                my_file.write(str("[]"))

            with open("Square.json", "w") as my_file:
                my_file.write(str("[]"))
        else:
            for x in list_objs:
                new_dict = x.to_dictionary()
                arr.extend(json.loads(cls.to_json_string([new_dict])))
                file_name = x.__class__.__name__

                with open(if"{file_name}.json", "w") as my_file:
                    my_file.write(json.dumps(arr))
