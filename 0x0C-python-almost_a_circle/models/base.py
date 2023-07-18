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

        return json.dumps(list_dictionaries)

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

    @classmethod
    def create(cls, **dictionary):
        """ convert dictionary to class instance
            Args:
                dictionary: a dict object
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(3, 1)

        if cls.__name__ == "Square":
            dummy = cls(3)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """ load data from json file and create new objects
            Return:
                  a list of instances.
        """
        arr = []
        if cls.__name__ == "Rectangle":
            try:
                with open("Rectangle.json", "r") as my_file:
                    data = my_file.read()
                    arr = cls.from_json_string(data)
            except Exception as e:
                arr = []
        if cls.__name__ == "Square":
            try:
                with open("Square.json", "r") as my_file:
                    data = my_file.read()
                    arr = cls.from_json_string(data)
            except Exception as e:
                arr = []

        if len(arr) == 0:
            return []

        new_arr = []
        for x in arr:
            obj = cls.create(**x)
            new_arr.append(obj)

        return new_arr
