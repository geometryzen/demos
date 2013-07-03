# e2ga-reversion.py
from blade import *

# Convenience functions for creating Blades.
def Scalar2(w):
    return Euclidean2(w, 0, 0, 0)

def Vector2(x, y):
    return Euclidean2(0, x, y, 0)

def Pseudoscalar2(s):
    return Euclidean2(0, 0, 0, s)

def explain(m):
    print str(m) + " is " + repr(m)
    return m

def showValue(name, x):
    print name + " => " + str(x)
    return x

i = Vector2(1,0)
j = Vector2(0,1)
x = Vector2(0,0)
I = Pseudoscalar2(1)
explain(i)
explain(j)
explain(x)

x = i * j
showValue("x", x)
showValue("+x", +x)
showValue("-x", -x)
showValue("~x", ~x)
