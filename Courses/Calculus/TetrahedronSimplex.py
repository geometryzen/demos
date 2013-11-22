'''
This program is used to illustrate the measure-boundary theorem for a 3-simplex (tetrahedron) in 3D Euclidean space.
The initial approach will be purely algebraic.
This will be later illustrated with 3D geometry.
Finally, it would be nice to prove the result symbolically.
'''
from e3ga import *
from math import *
from random import *

def randomInt():
    return int(random() * 100)

# Set up some basis vectors.
i = VectorE3(1.0, 0.0, 0.0)
j = VectorE3(0.0, 1.0, 0.0)
k = VectorE3(0.0, 0.0, 1.0)

# The tetrahedron is described by 4 points.
x0 = randomInt() * i + randomInt() * j + randomInt() * k
x1 = randomInt() * i + randomInt() * j + randomInt() * k
x2 = randomInt() * i + randomInt() * j + randomInt() * k
x3 = randomInt() * i + randomInt() * j + randomInt() * k

volume = (x1 - x0) ^ (x2 - x0) ^ (x3 - x0) / factorial(3)
print "directed volume measure of tetrahedron: " + str(volume)

# Now we calculate the directed measure of each of the faces.
a = -0.5 * (x1 - x0) ^ (x2 - x0)
print "directed measure of face (x0, x1, x2): " + str(a)
b = +0.5 * (x1 - x0) ^ (x3 - x0)
print "directed measure of face (x0, x1, x3): " + str(b)
c = -0.5 * (x2 - x0) ^ (x3 - x0)
print "directed measure of face (x0, x2, x3): " + str(c)
d = +0.5 * (x2 - x1) ^ (x3 - x1)
print "directed measure of face (x1, x2, x3): " + str(d)
print ""
print "directed measure of surface of tetrahedron: " + str(a+b+c+d)
