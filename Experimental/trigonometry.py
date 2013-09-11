from e2ga import *

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

def towards(fromVector, toVector, angle):
    return fromVector
