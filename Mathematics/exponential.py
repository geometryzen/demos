from e3ga import *
from math import exp, pi
from units import *

i = VectorE3(1,0,0)
j = VectorE3(0,1,0)
theta = (pi / 3) * i * j
omega = theta * (1 / second)

t = 1 * second
theta = omega * t
print "omega       => " + str(omega)
print "theta       => " + str(theta)
print "exp(theta)  => " + str(exp(theta))
# TODO: Measure does not support unary minus
# TODO: And multiplication by a number is broken.
print "exp(theta * +1) => " + str(exp(theta * +1))
print "exp(theta * -1) => " + str(exp(theta * -1))
# print "exp(theta * 1)  => " + str(exp(-theta))

R = exp(theta * -1)
r = R * (5 * i * meter) * (~R)

