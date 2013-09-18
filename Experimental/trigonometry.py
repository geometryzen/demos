from e2ga import *
from math import pi, sqrt, cos, sin
from units import *

def showValue(name, m):
    print name + " => " + str(m)
    return m

def showRepr(name, m):
    print name + " => " + repr(m)
    return m

# Create a few unit vectors to match the "compass" terminology in the question:
zero  = VectorE2(0, 0) * meter
north = VectorE2(0, 1) * meter
east  = VectorE2(1, 0) * meter
south = zero - north # Avoid issue with unimplemented unary minus!
west  = zero - east
showRepr("south", south)

def toRadians(deg):
    return deg * pi / 180

def towards(a, b, theta):
    '''
    Returns a vector which is the result of rotating a towards b by an angle theta.
    A fluid function rotate(a).towards(b).by(theta) would be interesting?
    '''
    # Perhaps should normalize the vectors a and b?
    # In fact, if don't normalize then the dimensions would be wrong.
    # Should generalize for non-orthogonal case?
    # Find a more elegant way to not have to mess with units?
    # Dropping the units on the floor seems a bit extreme.
    showRepr("a", a)
    showRepr("b", b)
    B =  a.quantity ^ b.quantity
    showRepr("B", B)
    c = cos(theta/2)
    s = sin(theta/2)
    Bs = B * s
    showRepr("Bs", Bs)
    return (c - Bs) * a.quantity * (c + Bs) * a.uom

d1 = 100 * east
showRepr("d1", d1)
d2 = 300 * south
d3 = 150 * towards(west, south, toRadians(30))
d4 = 200 * towards(west, north, toRadians(60))

d = d1 + d2 + d3 + d4

showValue("d1", d1)
showValue("d2", d2)
showValue("d3", d3)
showValue("d4", d4)
showValue("d1 + d2 + d3 + d4", d)