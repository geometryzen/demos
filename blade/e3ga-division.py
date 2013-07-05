# e3ga-division.py
from eight import *
from math import random, floor

def explain(m):
    print str(m) + " is " + repr(m)
    return m

def showValue(name, m):
    print name + " => " + str(m)
    return m

def ri():
    return floor(random())

zero = explain(Euclidean3(0, 0, 0, 0, 0, 0, 0, 0))
one  = explain(Scalar3(1))
two  = explain(Scalar3(2))
three= explain(3)
e1   = explain(Vector3(1, 0, 0))
e2   = explain(Vector3(0, 1, 0))
e3   = explain(Vector3(0, 0, 1))
e12  = explain(Bivector3(1, 0, 0))
e23  = explain(Bivector3(0, 1, 0))
e31  = explain(Bivector3(0, 0, 1))
I    = explain(Pseudoscalar3(1))

a = Euclidean3(ri(),ri(),ri(),ri(),ri(),ri(),ri(),ri())
showValue("a",a)

b = ~a
showValue("~a",b)

c = a * b
showValue("a * ~a", repr(c))

d = c * c
showValue("d", d)