#!/usr/bin/python3

from dis import dis

def magic_calculation(a: int, b: int):
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)

print(dis(magic_calculation))
