'''
A block slides down an inclined plane that makes a 30 degree angle with the horizontal.
If the coefficient of friction is 0.3, find the acceleration of the block.
'''
from math import *
from e3ga import *

# The given parameters
theta = (30 / 180) * pi
mu = 0.3

def acceleration(theta, mu):
    # First, compute the vector up the plane.
    eUp = VectoreE3(cos(theta), sin(theta), 0)
    
    
print acceleration(theta, mu)
