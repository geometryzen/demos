from e3ga import *
from units import *
 
m = ScalarE3(10.0) * kilogram
r = VectorE3(1.0, 0.0, 0.0) * meter
 
print "m => " + str(m)
 
g = 9.81 * VectorE3(0.0, 0.0, -1.0) * newton / kilogram
print "g => " + str(g)
 
F = m * g
 
print "F => " + str(F)

T = F ^ r
 
print "T => " + str(T)

print "T >> r => " + str(T >> r)
print "(T >> r)/(r * r) => " + str((T >> r)/(r * r))

print "r << T => " + str(r << T)
print "(r << T)/(r * r) => " + str((r << T)/(r * r))
