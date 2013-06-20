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

green = Color(0x00FF00)
print repr(green)
print "r: " + str(green.r)
print "g: " + str(green.g)
print "b: " + str(green.b)
print green


