#!/usr/bin/python3

# program to print number from 0 to 99
for x in range(100):
    if x < 99:
        print("{num:02d}".format(num=x), end=", ")
    else:
        print("{}".format(x))
