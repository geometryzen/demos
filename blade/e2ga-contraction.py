from e2ga import *
import math

def isCloseTo(expected, actual, precision):
    return math.fabs(expected - actual) < (math.pow(10, -precision) / 2)

def assertEqual(expect, actual, message):
    if expect != actual:
        print {"expect":expect,"actual":actual,"message":message}

def assertCloseTo(expect, actual, message):
    if expect != actual:
        print {"expect":expect,"actual":actual,"message":message}

# Convenience functions for creating Blades.
def Scalar(w):
    return Euclidean2(w, 0, 0, 0)

def Vector(x, y):
    return Euclidean2(0, x, y, 0)

def Pseudoscalar(s):
    return Euclidean2(0, 0, 0, s)

def explain(m):
    print str(m) + " is " + repr(m)
    return m

def showValue(name, x):
    print name + " => " + str(x)
    return x

z = explain(Euclidean2(0,0,0,0))
u = explain(Scalar(1))
d = explain(Scalar(2))
i   = explain(Vector(1, 0))
j   = explain(Vector(0, 1))
I   = explain(Pseudoscalar(1))

assertEqual(+z, ~z, str(z))
assertEqual(+u, ~u, str(u))
assertEqual(+i, ~i, str(i))
assertEqual(+j, ~j, str(j))
assertEqual(-I, ~I, str(I))

blades = [z, u, d, i, j, I]
for A in blades:
    print ""
    for B in blades:
        M = A << B
        Arev = ~A
        Brev = ~B
        N = ~((~A) >> (~B)) 
        assertEqual(M, N, str(A) + " << " + str(B) + " => "+ str(M) + ", S/B " + str(Arev) + " >> " + str(Brev) + str(N))
