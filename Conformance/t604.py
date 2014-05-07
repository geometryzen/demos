# This program examines the vector cross-product from a Geometric Algebra perspective
# and provides an alternative geometric formulation of the Lorentz force law.
# It is not a complete pedagogical analysis, only a glimpse of the computations.
from e3ga import *
from math import acos, fabs, pi, pow, sqrt

e1 = VectorE3(1.0, 0.0, 0.0)
e2 = VectorE3(0.0, 1.0, 0.0)
e3 = VectorE3(0.0, 0.0, 1.0)

def isCloseTo(expected, actual, precision):
    return fabs(expected - actual) < (pow(10, -precision) / 2)

def assertEqual(expect, actual, message):
    if expect != actual:
        print {"expect":expect,"actual":actual,"message":message}

def assertCloseTo(expect, actual, message):
    if not isCloseTo(expect, actual, 4):
        print {"expect":expect,"actual":actual,"message":message}

def makeCoord(n):
    return n

# Start with two random vectors a and b:
a = VectorE3(makeCoord(3.0), makeCoord(5.0), makeCoord(7.0))
b = VectorE3(makeCoord(2.0), makeCoord(4.0), makeCoord(6.0))

print "a => " + str(a)
print "b => " + str(b)

# Make a copy of a first because the cross method mutates its target.
c = a.clone().cross(b)
print "a cross b => " + str(c)

# We can now verify the three defining properties of the cross product in 3D.
print "1) a cross b is orthogonal to both b and c."
print "(a cross b).dot(a) => " + str(c.dot(a))
print "(a cross b).dot(b) => " + str(c.dot(b))
print "2) |a cross b| = |a||b|sin(theta), where theta is the angle between a and b."
# This takes a bit more work because we need a definition of the angle between a and b:
# a dot b = |a||b|cos(theta)
assertCloseTo(9.1104335791443, a.magnitude(), "|a|")
#assertCloseTo(7.4833147735478, b.magnitude()[0], "|b|")
assertEqual(68.0, a.dot(b), "a.dot(b)")
cosTheta = a.dot(b)/(a.magnitude()*b.magnitude())
#print "cos(theta) = " + str(cosTheta)
sinTheta = sqrt(1 - cosTheta * cosTheta)
#print "sin(theta) = " + str(sinTheta)
#print "|a cross b|= " + str(c.magnitude())
#print "|a||b|sin(theta)= " + str(a.magnitude() * b.magnitude() * sinTheta)
print "3) The direction of a cross b follows the right-hand rule."
i = VectorE3(1.0, 0.0, 0.0)
j = VectorE3(0.0, 1.0, 0.0)
k = VectorE3(0.0, 0.0, 1.0)
print "e1 cross e2 => " + str(e1.clone().cross(e2))
print "e2 cross e3 => " + str(e2.clone().cross(e3))
print "e3 cross e1 => " + str(e3.clone().cross(e1))
print "e2 cross e1 => " + str(e2.clone().cross(e1))
print "e3 cross e2 => " + str(e3.clone().cross(e2))
print "e1 cross e3 => " + str(e1.clone().cross(e3))
# Now lets talk about the Geometric Algebra approach.
print "e1, e2 and e3 are actually multivectors under the covers!"
print "repr(e1) => " + repr(e1)
print "repr(e2) => " + repr(e2)
print "repr(e3) => " + repr(e3)
I = PseudoscalarE3(1.0)
print "PseudoscalarE3(1) => " + str(I)
print "repr(PseudoscalarE3(1)) => " + repr(I)
print "e1 * e2 * e3 => " + str(e1 * e2 * e3)
dualB = -(b * I)
print "dual(b) => " + str(dualB)
print "repr(dual(b)) => " + repr(dualB)
print "a << dual(b) => " + str(a << dualB)
print "a cross b    => " + str(c)
# This is not just a coincidence! Verify it by trying a few random vectors.
# The properties of the cross product then follow from duality and contraction definitions.
# This insight allows us to dispense with axial vectors (those resulting from a cross product
# of polar vectors.
# Feynman called polar vectors "honest" because of their reflection symmetry properties.
# We can make all 3D vectors honest if we use vectors and bivectors appropriately.
# In the Lorentz Force Law, the part of the force resulting from v cross B is an "honest"
# vector because B is a "dishonest" vector. We should instead represent B by a bivector
# which is dual to the classical magnetic field. Then the Lorentz Force law becomes:
# F = q(E + v << B).
#
# This is, perhaps, suggestive that we recover an electric field by removing a velocity from
# the bivector magnetic field.
#
# An even tidier approach is to define the new magnetic field to be scaled by the speed of 
# light, then
# F = q(E + beta << B), where beta = v/c and B = I * B(traditional) * c
