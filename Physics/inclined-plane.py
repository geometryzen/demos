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

# Unit vectors that may be more useful to the problem.
eUp = cos(theta) * i + sin(theta) * j
eDown = -eUp
eNorm = eDown.cross(k)

# acceleration due to gravity
g = - 9.8 * j * meter / (second ** 2)
print "g => %s" % (g)

def acceleration(theta, mu):
    mass = 12345 * kilogram
    W = mass * g
    # The block does not rise above the plane nor sink into it.
    # The normal reaction plus the component of the weight normal to the plane must be zero.
    N = - W.dot(eNorm) * eNorm
    print "N => %s (normal to the incline)" % (N / eNorm)
    # The frictional force acts in the opposite direction to the velocity.
    # We assume the velocity to be down the incline.
    Friction = - magnitude(mu * N) * eDown
    print "Friction => %s (down the incline)" % (Friction/eDown)

    # Notice that I simply add the force due to friction because it has the correct direction.
    F = W.dot(eDown) * eDown + Friction
    print "F => %s (down the incline)." % (F/eDown)
    
    return F / mass
    
    
a = acceleration(theta, mu).dot(eDown)

print "a = %s" % (a)
