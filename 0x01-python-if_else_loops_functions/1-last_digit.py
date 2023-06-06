#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = 0
if number < 0:
    number = abs(number)
    last_digit = -abs(number % 10)
    number = -abs(number)
else:
    last_digit = number % 10

message = "and is 0"
if last_digit == 0:
    print(f"Last digit of {number} is {last_digit} {message}")
if last_digit > 5:
    message = "and is greater than 5"
    print(f"Last digit of {number} is {last_digit} {message}")
if last_digit < 6 and last_digit != 0:
    message = "and is less than 6 and not 0"
    print(f"Last digit of {number} is {last_digit} {message}")
