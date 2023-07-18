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
            return json.dumps([])
        else:
            return json.dumps(list(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ write Json string representation to file
        """

        arr = []

        if list_objs is None or len(list_objs) == 0:
            with open("Rectangle.json", "w") as my_file:
                my_file.write(str("[]"))

            with open("Square.json", "w") as my_file:
                my_file.write(str("[]"))
        else:
            for obj in list_objs:
                new_dict = obj.to_dictionary()
                arr.extend(json.loads(cls.to_json_string([new_dict])))
                file_name = obj.__class__.__name__

                with open(f"{file_name}.json", "w") as my_file:
                    my_file.write(json.dumps(arr))

    @staticmethod
    def from_json_string(json_string):
        """ convert json string to list
            Args:
                json_string: JSON string representation
            Return:
                a list of dictionaries else return an empty list
        """
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)
