#!/usr/bin/python3
import dis
"""
  magic_calculation - function to perfom math calculations
  @a: integer a
  @b: intger b
  @c: integer c

  Return: result to calculation
"""


def magic_calculation(a: int, b: int, c: int) -> int:

    if a < b:
        return c
    if c > b:
        return a + b

    return (a * b) - c
