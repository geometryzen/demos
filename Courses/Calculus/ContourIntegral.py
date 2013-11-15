'''
Experiment with the calculation and visualization of a path integral in the complex plane.

f(z) = 1/(z(z+1)), where the contour is a circle: |z| = R > 1.

We can convert this to polar coordinates and simplify.
We can also chug through the integral using Cartesian coordinates.

'''
from cmath import *

def f(z):
    return 1.0 / (z * (z + 1))

steps = 40
for i in range(0, steps):
    theta = i * 2 * pi / steps
    print i
    print theta

