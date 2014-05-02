from e3ga import *
from math import exp, pi
#from units import *

i = VectorE3(1.0, 0.0, 0.0)
j = VectorE3(0.0, 1.0, 0.0)
theta = (2.0 * pi) * i * j
omega = theta * (1 / second)
print "omega       => " + str(omega)

t = ScalarE3(1.0) * second
print "t           => " + str(t)
theta = omega * t
print "theta       => " + str(theta)
print "exp(theta)  => " + str(exp(theta))
print "exp(+theta) => " + str(exp(+theta))
print "exp(-theta) => " + str(exp(-theta))

R = exp(-theta / 2.0)
print "R           => " + str(R)
r = R * (1.0 * i * meter) * ~R

print r
