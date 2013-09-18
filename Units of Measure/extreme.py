# Work In Progress
from e3ga import *
from units import *
 
m = ScalarE3(10) * kilogram
r = VectorE3(1,0,0) * meter
 
print "m => " + str(m)
 
g = 9.81 * VectorE3(0, 0, -1) * newton / kilogram
print "g => " + str(g)
 
F = m * g
 
print "F => " + str(F)
 
T = F ^ r
 
print "T => " + repr(T)
print "T => " + str(T)

print "T >> r => " + repr(T >> r)
print "T >> r => " + str(T >> r)
print "(T >> r)/(r*r) => " + str((T >> r)/(r * r))
