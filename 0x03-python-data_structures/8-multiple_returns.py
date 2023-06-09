#!/usr/bin/python3

def multiple_returns(sentence: str) -> tuple:
    """  function that returns a tuple with the length,
         of a string and its first character

         Args:
             sentence: string value

         Return:
             a tuple with the length of string and,
             first character in string else return
             a tuple with the length and None as,
             the first character.
             (length, first character)
    """
    length = len(sentence)

    if length == 0:
        return (length, None)

    return (length, sentence[0])
