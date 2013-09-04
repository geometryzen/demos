from e3ga import *

g = VectorE3(0, 0, -9.81)

print "g => " + repr(g)

dt = 2

dv = g * dt

print "dv => " + repr(dv)

#print g * "hello"
