#!/usr/bin/python3

hidden = __import__("hidden_4")

if __name__ == "__main__":
    names = dir(hidden)
    for x in names:
        if not x.startswith("__"):
            print("{}".format(x))
