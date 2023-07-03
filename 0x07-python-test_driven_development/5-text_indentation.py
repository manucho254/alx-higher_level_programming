#!/usr/bin/python3

""" function that prints a text,
    with 2 new lines after each of these characters: ., ? and :
    Desc:
        - text must be a string, otherwise,
        raise a TypeError exception with the message text must be a string.
"""


def text_indentation(text: str) -> None:
    """ print a text with 2 new lines after each of,
        these characters: ., ? and :
        Args:
            text: string to find subtext to print
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    symbols = [".", "?", ":"]
    for x in symbols:
        text = text.replace(x, f"{x}\n\n")

    text = list(text)
    for j in range(len(text) - 1):
        if text[j] == "\n" and text[j + 1] == " ":
            text[j + 1] = ""

    print("".join(text), end="")
