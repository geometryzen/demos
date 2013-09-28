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

assertEqual(A.w, 0x0)
assertEqual(A.x, 0x1)
assertEqual(A.y, 0x2)
assertEqual(A.z, 0x4)
assertEqual(A.t, 0x8)

B = VectorL4(0x1, 0x2, 0x4, 0x8)

assertEqual(B.w, 0x0)
assertEqual(B.x, 0x1)
assertEqual(B.y, 0x2)
assertEqual(B.z, 0x4)
assertEqual(B.t, 0x8)

A = VectorL4(2, 3, 5, 7)
B = VectorL4(11,13,17,19)
C = A + B
assertEqual(C.w, 0)
assertEqual(C.x, 13)
assertEqual(C.y, 16)
assertEqual(C.z, 22)
assertEqual(C.t, 26)

C = A + 5
assertEqual(C.w, 5)
assertEqual(C.x, 2)
assertEqual(C.y, 3)
assertEqual(C.z, 5)
assertEqual(C.t, 7)

C = 5 + A
assertEqual(C.w, 5)
assertEqual(C.x, 2)
assertEqual(C.y, 3)
assertEqual(C.z, 5)
assertEqual(C.t, 7)

five = ScalarL4(5)

C = A + five
assertEqual(C.w, 5)
assertEqual(C.x, 2)
assertEqual(C.y, 3)
assertEqual(C.z, 5)
assertEqual(C.t, 7)

C = five + A
assertEqual(C.w, 5)
assertEqual(C.x, 2)
assertEqual(C.y, 3)
assertEqual(C.z, 5)
assertEqual(C.t, 7)

X = VectorL4(3, 4, 12, 13)
assertEqual(X.quadrance(), 25)

print "Done!"
