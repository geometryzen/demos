# This program examines the vector cross-product from a Geometric Algebra perspective
# and provides an alternative geometric formulation of the Lorentz force law.
from eight import *
from math import random

# Start with two random vectors a and b:
a = Vector3(random(), random(), random())
b = Vector3(random(), random(), random())

print "a=" + str(a)
print "b=" + str(b)

