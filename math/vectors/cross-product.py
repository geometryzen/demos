# This program examines the vector cross-product from a Geometric Algebra perspective
# and provides an alternative geometric formulation of the Lorentz force law.
# It is not a complete pedagogical analysis, only a glimpse of the computations.
from e3ga import *
from math import acos, pi, sqrt

def makeCoord(n):
    return n

# Start with two random vectors a and b:
a = VectorE3(makeCoord(3), makeCoord(5), makeCoord(7))
b = VectorE3(makeCoord(2), makeCoord(4), makeCoord(6))

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
print "|a| => " + str(a.length())
print "|b| => " + str(b.length())
print "a.dot(b) => " + str(a.dot(b))
cosTheta = a.dot(b)/(a.length()*b.length())
print "cos(theta) = " + str(cosTheta)
sinTheta = sqrt(1 - cosTheta * cosTheta)
print "sin(theta) = " + str(sinTheta)
print "|a cross b|= " + str(c.length())
print "|a||b|sin(theta)= " + str(a.length() * b.length() * sinTheta)
print "3) The direction of a cross b follows the right-hand rule."
i = VectorE3(1, 0, 0)
j = VectorE3(0, 1, 0)
k = VectorE3(0, 0, 1)
print "i cross j => " + str(i.clone().cross(j))
print "j cross k => " + str(j.clone().cross(k))
print "k cross i => " + str(k.clone().cross(i))
print "j cross i => " + str(j.clone().cross(i))
print "k cross j => " + str(k.clone().cross(j))
print "i cross k => " + str(i.clone().cross(k))
# Now lets talk about the Geometric Algebra approach.
print "i, j and k are actually multivectors under the covers!"
print "repr(i) => " + repr(i)
print "repr(j) => " + repr(j)
print "repr(k) => " + repr(k)
I = Pseudoscalar3(1)
print "Pseudoscalar3(1) => " + str(I)
print "repr(Pseudoscalar3(1)) => " + repr(I)
print "ijk => " + str(i * j * k)
dualB = b/I
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
