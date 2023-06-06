#!/usr/bin/python3

for x in range(10):
    for i in range(x, 10):
        if x != i:
            if x != 8 or i != 9:
                print("{}{}".format(x, i), end=", ")
            else:
                print("{}{}".format(x, i))
