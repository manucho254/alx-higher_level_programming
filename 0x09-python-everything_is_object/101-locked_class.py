#!/usr/bin/python3

""" class that prevents the user from,
   dynamically creating new instance attributes,
   except if the new instance attribute is called first_name
"""


class LockedClass:
    """ defines class LockedClass
    """
    def __setattr__(self, name, value):
        """ setter to set new firstname
            Args:
                name: name of the new attribute
                value: value for new attribute
        """
        if name == "first_name":
            self.__dict__[name] = value
        else:
            message = f"'LockedClass' object has no attribute '{name}'"
            raise AttributeError(message)
