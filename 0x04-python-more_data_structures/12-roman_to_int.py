#!/usr/bin/python3

def roman_to_int(roman_string: str) -> int:
    """function that converts a Roman numeral to an integer.

       Args:
           roman_string: a string

       Return:
           an integer representation of the,
           roman numeral string else return 0
    """

    if type(roman_string) != str or not roman_string:
        return 0

    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = []

    for val in roman_string:
        result.append(roman[val])

    while result != sorted(result, reverse=True):
        for x in range(len(result) - 1):
            if result[x] < result[x + 1]:
                result[x] = result[x + 1] - result[x]
                result[x + 1] = 0

    return sum(result)
