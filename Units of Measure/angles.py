from units import *
from math import *

length0 = 1.0 * meter
angle1 = pi * radian
angle2 = 180 * degree

print length0
print angle1
print angle2

print "cos(angle1) %s" % cos(angle1)
print "cos(angle2) %s" % cos(angle2)

print angle1 + angle2

# It will quite happily do this!
print type(2 * radian)
print sqrt(2 * radian)
print cos(sqrt(angle1 * angle1))
print cos(meter)