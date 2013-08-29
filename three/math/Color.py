# Color demonstration.
from eight import *

color = Color()

print repr(color)
print "r: " + str(color.r)
print "g: " + str(color.g)
print "b: " + str(color.b)
print color
color.r = 0.1
color.g = 0.2
color.b = 0.3
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

blue = Color(0x00FF00)
print repr(blue)
print "r: " + str(blue.r)
print "g: " + str(blue.g)
print "b: " + str(blue.b)
print blue

colors = [Color("rgb(250,0,0)"),Color("rgb(100%,0%,0%)"), Color("#ff0000"),Color("#f00"),Color("red")]
for c in colors:
    print c
    
x = Color(color)
print "x: " + repr(x)

x.setRGB(0.0, 1.0, 0.0)
print "x: " + repr(x)


