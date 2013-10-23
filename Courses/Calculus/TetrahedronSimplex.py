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

x0 = VectorE3(0,0,0)
x1 = i + 3 * j
x2 = j
x3 = k

volume = (x1 - x0) ^ (x2 - x0) ^ (x3 - x0) / factorial(3)
print "directed volume measure of tetrahedron: " + str(volume)
