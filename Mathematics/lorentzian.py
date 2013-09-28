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

A = Lorentzian(0x0,0x1,0x2,0x3,0x4,0x5,0x6,0x7,0x8,0x9,0xA,0xB,0xC,0xD,0xE,0xF)

assertEqual(A.x, 0x1)
assertEqual(A.y, 0x2)
assertEqual(A.z, 0x4)
assertEqual(A.t, 0x8)

B = VectorL4(0x1, 0x2, 0x4, 0x8)

assertEqual(B.x, 0x1)
assertEqual(B.y, 0x2)
assertEqual(B.z, 0x4)
assertEqual(B.t, 0x8)

print "Done!"
