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

a = Euclidean2(ri(),ri(),ri(),ri())
showValue("a", a)
#a = a[0] + a[2]
#showValue("a", a)

twiddleA = ~a
showValue("~a", twiddleA)

c = a * twiddleA
showValue("a * ~a", c)

d = c * c
showValue("d", d)
