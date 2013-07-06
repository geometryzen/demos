from e2ga import *
from math import random, floor

def explain(m):
    print str(m) + " is " + repr(m)
    return m

def showValue(name, m):
    print name + " => " + repr(m)
    return m

def ri():
    return floor(100*random())

a = Euclidean2(ri(),ri(),ri(),ri())
showValue("a", a)
a = a[0] + a[2]
showValue("a", a)

twiddleA = ~a
showValue("~a", twiddleA)

c = a * twiddleA
showValue("a * ~a", repr(c))

showValue("(a * ~a)[0]", repr(c[0]))

d = c * c
showValue("d", d)

e = d * d
showValue("e", e)

f = e * e
showValue("f", f)

print Euclidean2(0,1,0,0) * Euclidean2(0,0,1,0)
