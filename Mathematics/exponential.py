from e3ga import *
from math import exp, pi
from units import *

i = VectorE3(1,0,0)
j = VectorE3(0,1,0)
theta = (pi / 3) * i * j
omega = theta * (1 / second)

t = ScalarE3(1) * second
theta = omega * t
print "omega       => " + str(omega)
print "theta       => " + str(theta)
print "exp(theta)  => " + str(exp(theta))
print "exp(+theta) => " + str(exp(+theta))
print "exp(-theta) => " + str(exp(-theta))

R = exp(-theta/2)
r = R * (5 * i * meter) * ~R

print r
print r.quantity

