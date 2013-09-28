'''
UNDER CONSTRUCTION
Lorentzian is a Geometric Algebra multivector (quantity) with a metric that is Lorentzian.
'''
from lorentz import *
# The following functions are provided for testing purposes.

def assertEqual(actual, expect):
    if expect == actual:
        pass
    else:
        print {"actual": actual, "expect": expect}

def assertTrue(actual):
    return assertEqual(actual, True)

def assertFalse(actual):
    return assertEqual(actual, False)

def explain(m):
    print str(m) + " is " + repr(m)
    return m

def showValue(name, m):
    print name + " => " + str(m)
    return m

def isCloseTo(actual, expect):
    epsilon = 1e-10
    error = actual - expect
    quadrance = error % error
    return sqrt(quadrance) < epsilon

A = VectorL4(2, 3, 5, 7)
B = VectorL4(11,13,17,19)

assertEqual(A.x, 2)
assertEqual(A.y, 3)
assertEqual(A.z, 5)
