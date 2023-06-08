#!/usr/bin/python3
for x in range(65, 91):
    print("{}".format(chr(x) if x < 90 else chr(x) + "\n"), end="")
