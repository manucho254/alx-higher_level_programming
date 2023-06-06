#!/usr/bin/python3
import random

number = random.randint(-10, 10)
if number > 0:  # check if number is positive
    print("is positive")
if number == 0:  # check if number is zero
    print("is zero")
if number < 0:  # check if number is negative
    print("is negative")
