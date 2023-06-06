#!/usr/bin/python3

# program to reverse alphabets
for x in range(122, 96, -1):
    ch = x
    if x % 2 != 0:
        ch = (ch - 32)
    print("{}".format(chr(ch)), end="")
