# This program examines the vector cross-product from a Geometric Algebra perspective
# and provides an alternative geometric formulation of the Lorentz force law.
from eight import *
from math import random, acos, pi, sqrt

def makeCoord(n):
    return n
    # return random()

# Start with two random vectors a and b:
a = Vector3(makeCoord(3), makeCoord(5), makeCoord(7))
b = Vector3(makeCoord(2), makeCoord(4), makeCoord(6))

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
i = Vector3(1, 0, 0)
j = Vector3(0, 1, 0)
k = Vector3(0, 0, 1)
print "i cross j => " + str(i.clone().cross(j))
print "j cross k => " + str(j.clone().cross(k))
print "k cross i => " + str(k.clone().cross(i))
print "j cross i => " + str(j.clone().cross(i))
print "k cross j => " + str(k.clone().cross(j))
# Now lets talk about the Geometric Algebra approach.
print "repr(i) => " + repr(i)
print "repr(j) => " + repr(j)
print "repr(k) => " + repr(k)
I = Pseudoscalar3(1)
print I
print repr(I)
dualB = -(b * I)
print "dual(B) => " + str(dualB)
print "repr(dual(B)) => " + repr(dualB)
print "a << dualB => " + str(a << dualB)


