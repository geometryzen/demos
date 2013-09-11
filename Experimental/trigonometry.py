from e2ga import *
from math import pi, sqrt

def showValue(name, m):
    print name + " => " + str(m)
    return m

north = VectorE2(0, 1)
east = VectorE2(1, 0)
south = -north
west = -east

showValue("north", north)
showValue("south", south)
showValue("east", east)
showValue("west", west)

def toRadians(deg):
    return deg * pi / 180

def towards(a, b, angle):
    print 1 + b << a
    R = (1 + a * b) / sqrt(1 + a << b)
    return fromVector

showValue("east towards south by 30 degrees", towards(east, south, toRadians(30)))
