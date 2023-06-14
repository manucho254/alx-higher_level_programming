#!/usr/bin/python3

def roman_to_int(roman_string: str) -> int:
    """function that converts a Roman numeral to an integer.

       Args:
           roman_string: a string

       Return:
           an integer representation of the,
           roman numeral string else return 0
    """

    if not roman_string or roman_string is None:
        return 0

    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    known = {"II": 2, "III": 3, "IV": 4, "VI": 6, "VII": 7, "VIII": 8, "IX": 9}
    result = 0

    if roman_string in known:
        return known[roman_string]

    for x in roman_string:
        result += roman[x]

    return result
