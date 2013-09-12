# Work In Progress.
# TODO: Arranging things so that the order of units, multivectors does not matter.
from e2ga import *
from math import pi, sqrt, cos, sin
from units import * # See if we can perform the calculations using measures?

def showValue(name, m):
    print name + " => " + str(m)
    return m

# Create a few unit vectors to match the "compass" terminology in the question:
north = VectorE2(0, 1)
east = VectorE2(1, 0)
south = -north
west = -east

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
    B =  a ^ b
    c = cos(theta/2)
    s = sin(theta/2)
    return (c - B * s) * a * (c + B * s)

d1 = 100 * east
d2 = 300 * south
d3 = 150 * towards(west, south, toRadians(30))
d4 = 200 * towards(west, north, toRadians(60))

x1 = 100 * east * meter
x2 = ScalarE2(300) * south * meter
x3 = ScalarE2(150) * towards(west, south, toRadians(30)) * meter
x4 = ScalarE2(200) * towards(west, north, toRadians(60)) * meter
showValue("x1", x1)
showValue("x2", x2)

d = d1 + d2 + d3 + d4

showValue("d1", d1)
showValue("d2", d2)
showValue("d3", d3)
showValue("d4", d4)
showValue("answer", d)