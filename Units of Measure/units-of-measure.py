from e3ga import *
from units import *
from math import *
 
m = ScalarE3(10.0) * kilogram
 
print "m => " + str(m)
 
g = 9.81 * VectorE3(0.0, 0.0, -1.0) * newton / kilogram
print "g => " + str(g)
 
F = m * g
 
print "F => " + str(F)
 
a = F / m

print "a => " + str(a)

print kilogram * g * second

k = 2 * newton / meter

print "k => " + str(k)

# TODO: sqrt as a universal function
print type(k/m)
omega = sqrt(k / m)

#TODO: Pow for Euclidean3 and float.

print "k/m => " + str(k/m)

#
omega = (k / m) ** 0.5

# Interesting, we've really got rad/s here.
print omega