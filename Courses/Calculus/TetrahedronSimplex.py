'''
This program is used to illustrate some theorems for simplices in the case of a 3-simplex (tetrahedron) in 3D Euclidean space.
The initial approach will be purely alhebraic.
This will be later illustrated with 3D geometry.
Finally, it would be nice to prove the result symbolically.
'''
from e3ga import *

# Let the tetrahedron be described by 4 points.
# For simplicity we will use a standard simplex.
i = VectorE3(1,0,0)
x0 = VectorE3()