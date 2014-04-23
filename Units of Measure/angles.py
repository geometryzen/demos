from e3ga import *
from units import *
from math import pi, cos

angle1 = pi * radian
angle2 = 180 * degree

print angle1
print angle2

print repr(angle1)
print type(angle1.quantity)
print "cos(angle1)", cos(angle1)
print "cos(angle2)", cos(angle2)

print angle1 + angle2

