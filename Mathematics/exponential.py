from e3ga import *
from math import exp, pi
from units import *

i = VectorE3(1,0,0)
print "i           => " + repr(i)
j = VectorE3(0,1,0)
print "j           => " + repr(j)
theta = (2 * pi) * i * j
print "theta       => " + repr(theta)
omega = theta * (1 / second)
print "omega       => " + repr(omega)
print "omega       => " + str(omega)

t = ScalarE3(1) * second
print "t           => " + repr(t)
print "t           => " + str(t)
theta = omega * t
print "theta       => " + str(theta)
print "exp(theta)  => " + str(exp(theta))
print "exp(+theta) => " + str(exp(+theta))
print "exp(-theta) => " + str(exp(-theta))

R = exp(-theta/2)
r = R * (1 * i * meter) * ~R

print r
