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
    denom = 2 * (1 + (b << a)).w
    print repr(denom)
    R = (1 + a * b) / sqrt(denom)
    print repr(R)
    return b

showValue("east towards south by 30 degrees", towards(east, south, toRadians(30)))
