'''
A block slides down an inclined plane that makes a 30 degree angle with the horizontal.
If the coefficient of friction is 0.3, find the acceleration of the block.
'''
# We'll be using some trigonometry to handle the angles.
from math import *
# We'll be economical in our processing and use only 2D quantities.
from e2ga import *
# We'll use units throughout and let the software do the manipulations.
from units import *

# Define standard orthogonal unit vectors and their meanings.
# Although the incline also provides a natural frame, I find it easier
# to think of gravity as being simply down in this situation.
i  = VectorE2(1,0) # To the right.
j  = VectorE2(0,1) # Up

# The given parameters
theta = (30.0 / 180.0) * pi
mu = 0.3

# Unit vectors that may be more useful to the problem.
eUp = cos(theta) * i + sin(theta) * j
eDown = -eUp
# One-sided multiplication will work correctly in two dimensions to produce a rotation.
eNorm = eDown * i * j

# acceleration due to gravity
g = - 9.8 * j * meter / (second ** 2)

def acceleration(theta, mu):
    # Analytically, the result in this case is independent of the mass.
    # We're using lowercase quantities to show that mass has been divided out.
    # Quantities which were forces are now accelerations.
    mass = 12345 * kilogram * second
    W = mass * g

    # The block does not rise above the plane nor sink into it.
    # The normal reaction plus the component of the weight normal to the plane must be zero.
    N = - W.dot(eNorm) * eNorm
    # The frictional force acts in the opposite direction to the velocity.
    # We assume the velocity to be down the incline.
    Friction = magnitude(mu * N) * eUp

    # Notice that I simply add the force due to friction because it has the correct direction.
    F = (W << eDown) * eDown + Friction
    
    return F / mass
    
a = acceleration(theta, mu)

print "a << down = %s (down the plane)"      % (a << eDown)
print "a << norm = %s (normal to the plane)" % (a << eNorm)
