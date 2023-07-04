import ctypes

a = 1
aid = id(a)
print(aid)
print(ctypes.cast(aid, ctypes.py_object).value)
b = 1
aid = id(b)
print(aid)
print(ctypes.cast(aid, ctypes.py_object).value)
