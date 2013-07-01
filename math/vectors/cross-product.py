# This program examines the vector cross-product from a Geometric Algebra perspective
# and provides an alternative geometric formulation of the Lorentz force law.
from eight import *

# Start with two example vectors a and b:
a = Vector3(1, 3, 5)
b = Vector3(7, 11, 13)

print "a => " + str(a)
print "b => " + str(b)

# Make a copy of a first because the cross method mutates its target.
c = a.clone().cross(b)
print "a => " + str(a)
print "b => " + str(b)
print "c => " + str(c)

# We can now verify the three defining properties of the cross product in 3D.
# 1) c is orthogonal to both b and c
print "c.dot(a) => " + str(c.dot(a))

