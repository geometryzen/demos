from math import *
from units import *

omega = 2 * pi / (10 * second)

print omega

t = 5000 * milli * second

print repr(t)
print t

angle = omega * t

print repr(angle)
print angle

#c = cos(angle)
#print repr(c)
#s = sin(angle)
#print s

