# Color demonstration.
from three import *

color = Color()

print repr(color)
print "r: " + str(color.r)
print "g: " + str(color.g)
print "b: " + str(color.b)
print color

red = Color(0xFF0000)
print repr(red)
print "r: " + str(red.r)
print "g: " + str(red.g)
print "b: " + str(red.b)
print red
