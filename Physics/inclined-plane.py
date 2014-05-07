'''
A block slides down an inclined plane that makes a 30 degree angle with the horizontal.
If the coefficient of friction is 0.3, find the acceleration of the block.
'''
from math import *
from e3ga import *

# Define the ortogonal unit vectors and their meanings.
eDown   = VectorE3(1,0,0) # Down the incline (x).
eNormal = VectorE3(0,1,0) # Normal to the incline (y).
eInPage = VectorE3(0,0,1) # Into the page (z)

# The given parameters
theta = (30 / 180) * pi
mu = 0.3

def acceleration(theta, mu):
    F = W.dot(eDown) * eDown
    
    
print acceleration(theta, mu)
