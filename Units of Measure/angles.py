from units import *
from math import *
from e3ga import *
from e2ga import *

length0 = 1.0 * meter
angle1 = pi * radian
angle2 = ScalarE3(180) * degree
angle3 = ScalarE2(180) * degree

print length0
print angle1
print angle2
print angle3

print "cos(angle1) %s" % cos(angle1)
print "cos(angle2) %s" % cos(angle2)
print "cos(angle3) %s" % cos(angle3)

print "sin(angle1) %s" % sin(angle1)
print "sin(angle2) %s" % sin(angle2)
print "sin(angle3) %s" % sin(angle3)

print angle1 + angle2
print angle1 + angle3

print cos(sqrt(angle1 * angle1))
print cos(sqrt(angle2 * angle2))
print cos(sqrt(angle3 * angle3))

print acos(cos(angle1))
print acos(cos(angle2))
print acos(cos(angle3))

print asin(sin(angle1))
print asin(sin(angle2))