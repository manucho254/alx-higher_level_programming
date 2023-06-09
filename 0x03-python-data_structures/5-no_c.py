#!/usr/bin/python3

def no_c(my_string: str) -> str:
    """ function to replace all instances of,
        lowercase and uppercase c

        Args:
            my_sting: string to remove all c's

        Return:
             new string
    """

    return "".join([x for x in my_string if x != "c" and x != "C"])
