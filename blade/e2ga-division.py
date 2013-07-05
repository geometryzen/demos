# e2ga-division.py
from e2ga import *
from math import random, floor

def explain(m):
    print str(m) + " is " + repr(m)
    return m

def showValue(name, m):
    print name + " => " + str(m)
    return m

def ri():
    return floor(100*random())

# A general multivector (in 3D at least) has a path to inversion.
a = Euclidean2(ri(),ri(),ri(),ri())
# A spinor in 3D is more direct.
#a = Euclidean3(ri(),0,0,0,ri(),ri(),ri(),0)
showValue("a",a)

b = ~a
showValue("~a",b)

c = a * b
showValue("a * ~a", repr(c))

d = c * c
showValue("d", d)

print Euclidean2(0,1,0,0) * Euclidean2(0,0,1,0)
