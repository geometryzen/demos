'''
This program is used to illustrate some theorems for simplices in the case of a 3-simplex (tetrahedron) in 3D Euclidean space.
The initial approach will be purely alhebraic.
This will be later illustrated with 3D geometry.
Finally, it would be nice to prove the result symbolically.
'''
from e3ga import *
from math import *

# Let the tetrahedron be described by 4 points.
# For simplicity we will use a standard simplex.
i = VectorE3(1,0,0)
j = VectorE3(0,1,0)
k = VectorE3(0,0,1)

x0 = VectorE3(1,2,3)
x1 = i + 3 * j
x2 = j + 4 * k
x3 = i + j + k

volume = (x1 - x0) ^ (x2 - x0) ^ (x3 - x0) / factorial(3)
print "directed volume measure of tetrahedron: " + str(volume)

# Now we calculate the directed measure of each of the faces.
a = -0.5 * (x1 - x0) ^ (x2 - x0)
print "directed measure of face (x0, x1, x2): " + str(a)
b = +0.5 * (x1 - x0) ^ (x3 - x0)
print "directed measure of face (x0, x1, x3): " + str(b)
c = -0.5 * (x2 - x0) ^ (x3 - x0)
print "directed measure of face (x0, x1, x3): " + str(c)
d = +0.5 * (x2 - x1) ^ (x3 - x1)
print "directed measure of face (x0, x1, x3): " + str(d)
print ""
print "directed measure of surface of tetrahedron: " + str(a+b+c+d)
