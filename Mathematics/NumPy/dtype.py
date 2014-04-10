import numpy as np

def baz():
    return 3


a = np.array([1, 4, 5, 8], baz)
print a
print type(a)
print a[0]
print type(a[0])