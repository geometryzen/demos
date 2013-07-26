from eight import *
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

z = explain(Euclidean3(0, 0, 0, 0, 0, 0, 0, 0))
u = explain(Scalar3(1))
d = explain(Scalar3(2))
i   = explain(Vector3(1, 0, 0))
j   = explain(Vector3(0, 1, 0))
k   = explain(Vector3(0, 0, 1))
ij  = explain(Bivector3(1, 0, 0))
jk  = explain(Bivector3(0, 1, 0))
ki  = explain(Bivector3(0, 0, 1))
I   = explain(Pseudoscalar3(1))

assertEqual(+z, ~z, str(z))
assertEqual(+u, ~u, str(u))
assertEqual(+i, ~i, str(i))
assertEqual(+j, ~j, str(j))
assertEqual(-ij, ~ij, str(I))
assertEqual(-jk, ~jk, str(I))
assertEqual(-ki, ~ki, str(I))
assertEqual(-I, ~I, str(I))

blades = [z, u, d, i, j, k, ij, jk, ki, I]
for A in blades:
    print ""
    for B in blades:
        M = B >> A
        Ms = str(B) + ">>" + str(A) + "=>"+ str(M)
        N = ~((~A) << (~B))
        Ns = "~(~" + str(A) + "<<~" + str(B) + ")=>" + str(N)
        assertEqual(M, N, Ms  + " " + Ns)
