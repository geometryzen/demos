# This program examines the vector cross-product from a Geometric Algebra perspective
# and provides an alternative geometric formulation of the Lorentz force law.
from eight import *
from math import random, acos, pi

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
# 1) a cross b is orthogonal to both b and c
print "(a cross b).dot(a) => " + str(c.dot(a))
print "(a cross b).dot(b) => " + str(c.dot(b))
# 2) |a cross b| = |a||b|sin(theta), where theta is angle between  a and b.
# This takes a bit more work because we need a definition of the angle between a and b:
# a dot b = |a||b|cos(theta)
print "|a| => " + str(a.length())
print "|b| => " + str(b.length())
print "a.dot(b) => " + str(a.dot(b))
cosTheta = a.dot(b)/(a.length()*b.length())
print "cos(theta) = " + str(cosTheta)


