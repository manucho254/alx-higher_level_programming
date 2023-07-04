#!/usr/bin/python3
def magic_string(arr: list = []):
    arr.append(0)
    return "BestSchool, " * (len(arr) - 1) + "BestSchool"
