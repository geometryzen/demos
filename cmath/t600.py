from cmath import *
import math

print complex(1,0) * "hello"

def isCloseTo(expected, actual, precision):
    return math.fabs(expected - actual) < (math.pow(10, -precision) / 2)

def assertEqual(expect, actual, message):
    if expect != actual:
        print {"expect":expect,"actual":actual,"message":message}

def assertCloseTo(expect, actual, message):
    if expect != actual:
        print {"expect":expect,"actual":actual,"message":message}

print "----------"
print "construction"
print "----------"
z1 = complex(11, 7)
print "z1 = complex(11, 7)"
print "----------"
print "properties"
print "----------"
print "z1.real => " + str(z1.real)
print "z1.imag => " + str(z1.imag)
print "----------"
print "representations"
print "----------"
print "str(z1)  => " + str(z1)
print "repr(z1) => " + repr(z1)
print "----------"
print "type"
print "----------"
print "str(type(z1))  => " + str(type(z1))
print "repr(type(z1)) => " + repr(type(z1))
print "----------"
print "construction"
print "----------"
z2 = complex(5, 3)
print "z1 = complex(5, 3)"
print "----------"
print "z1 + z2 => " + str(z1 + z2)
print "z1 - z2 => " + str(z1 - z2)
print "z1 * z2 => " + str(z1 * z2)
print "z1 / z2 => " + str(z1 / z2)
print "----------"
print "z1 == z1 => " + str(z1 == z1)
print "z1 != z1 => " + str(z1 != z1)
print "z1 == z2 => " + str(z1 == z2)
print "z1 != z2 => " + str(z1 != z2)
print "----------"
assertCloseTo(math.pi, phase(complex(-1.0, 0.0)), "phase(-1)")
