'''
A block slides down an inclined plane that makes a 30 degree angle with the horizontal.
If the coefficient of friction is 0.3, find the acceleration of the block.
'''
from math import *
from e3ga import *
from units import *

# Define standard orthogonal unit vectors and their meanings.
# Although the incline also provides a natural frame, I find ut easier
# to think of gravity as being simply down in this situation.
i = VectorE3(1,0,0) # To the right.
j = VectorE3(0,1,0) # Up
k = i.cross(j)      # Must be out of page for a right-handed set.
print "k => %s" % (k)

# The given parameters
theta = (30.0 / 180.0) * pi
mu = 0.3

# acceleration due to gravity
g = - 9.8 * j * meter / (second ** 2)
print "g => %s" % (g)

def acceleration(theta, mu):
    eUp = cos(theta) * i + sin(theta) * j
    eDown = -eUp
    print "eDown => %s" % (eDown)
    m = 23 * kilogram
    print "m => %s" % (m)
    W = m * g
    print "W => %s" % (W)
    eNorm = eDown.cross(k)
    N = W.dot(eNorm) * eNorm
    print "N => %s" % (N / eNorm)
    # The frictional force acts in the opposite direction to the velocity.
    # We assume the velocity to be down the incline.
    Friction = magnitude(mu * N) * eDown
    print "Friction => %s" % (Friction)

    F = W.dot(eDown) * eDown
    print "F => %s" % (F/eDown)
    
    
print acceleration(theta, mu)
