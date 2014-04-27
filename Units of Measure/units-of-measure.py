from e3ga import *
from units import *
 
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

m = 5 * kilogram

omega = k / m

print omega