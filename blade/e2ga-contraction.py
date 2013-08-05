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

def explain(m):
    print str(m) + " is " + repr(m)
    return m

def showValue(name, x):
    print name + " => " + str(x)
    return x

z = explain(Euclidean2(0,0,0,0))
u = explain(Scalar2(1))
d = explain(Scalar2(2))
i   = explain(Vector2(1, 0))
j   = explain(Vector2(0, 1))
I   = explain(Pseudoscalar2(1))

assertEqual(+z, ~z, str(z))
assertEqual(+u, ~u, str(u))
assertEqual(+i, ~i, str(i))
assertEqual(+j, ~j, str(j))
assertEqual(-I, ~I, str(I))

blades = [z, u, d, i, j, I]
for A in blades:
    print ""
    for B in blades:
        M = B >> A
        Ms = str(B) + ">>" + str(A) + "=>"+ str(M)
        N = ~((~A) << (~B))
        Ns = "~(~" + str(A) + "<<~" + str(B) + ")=>" + str(N)
        assertEqual(M, N, Ms  + " " + Ns)
