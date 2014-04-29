from e3ga import *
from units import *
from math import *
 
mass = ScalarE3(10.0) * kilogram
 
print "mass => " + str(mass)
 
g = 9.81 * VectorE3(0.0, 0.0, -1.0) * newton / kilogram
print "g => " + str(g)
 
F = mass * g
 
print "F => " + str(F)
 
a = F / mass

print "a => " + str(a)

print kilogram * g
print (kilogram * g) * second

k = 2 * newton / meter

print "k => " + repr(k)

omega = sqrt(k / mass)

print "k/mass => " + str(k/mass)
print "sqrt(k/mass) => " + str(sqrt(k/mass))

omega = (k / mass) ** 0.5

# Interesting, we've really got rad/s here.
print omega
print omega * second