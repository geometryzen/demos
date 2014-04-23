from math import *
from units import *

omega = 2 * pi * radian / (10 * second)

print omega

t = 5000 * milli * second

print t

angle = omega * t

print angle

#print type(angle)
#print repr(angle)
print "cos(%s) -> %s" % (angle, cos(angle))
print "sin(%s) -> %s" % (angle, sin(angle))

#s = sin(angle)
#print s

