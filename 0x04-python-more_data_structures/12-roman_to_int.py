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
    result = []

    for val in roman_string:
        result.append(roman[val])

    for x in range(len(result) - 1):
        if result[x] < result[x + 1]:
            result[x] = result[x + 1] - result[x]
            result[x + 1] = 0

    for i in range(len(result) - 1):
        if result[i] < result[i + 1]:
            result[i] = result[i + 1] - result[i]
            result[i + 1] = 0

    for i in range(len(result) - 1):
        if result[i] < result[i + 1]:
            result[i] = result[i + 1] - result[i]
            result[i + 1] = 0

    return sum(result)
