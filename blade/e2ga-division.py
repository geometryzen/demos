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

def cc(A):
    return Euclidean2(A.w, -A.x, -A.y, -A.xy)

def inv(M):
    m = M * ~M
    x = ~M * cc(m)
    return x

A = Euclidean2(ri(),ri(),ri(),ri())
showValue("A", A)

showValue("inv(A)", inv(A))

showValue("A * inv(A)", A * inv(A))
