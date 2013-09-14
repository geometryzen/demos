from e3ga import *
from math import exp, pi
from units import *

i = VectorE3(1,0,0)
j = VectorE3(0,1,0)
theta = (pi / 3) * i * j
omega = theta * (1 / second)

t = second
theta = omega * t
print repr(theta)
print "omega => " + str(omega)
print "theta => " + str(theta)
print repr(exp(theta))

