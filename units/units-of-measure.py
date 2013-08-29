from e3ga import *
from units import kilogram, meter, second, newton, joule, watt
 
m = Scalar3(10) * kilogram
 
print "m => " + str(m)
 
g = 9.81 * Vector3(0, 0, -1) * newton / kilogram
print "g => " + str(g)
 
F = m * g
 
print "F => " + str(F)
 
a = F / m
 
print "a => " + str(a)