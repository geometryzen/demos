'''
Experiment with the calculation and visualization of a path integral in the complex plane.

f(z) = 1/(z(z+1)), where the contour is a circle: |z| = R > 1.

We can convert this to polar coordinates and simplify.
We can also chug through the integral using Cartesian coordinates.

'''
from cmath import *
from math import cos, sin, pi, tao

one = complex(1.0, 0.0)
i = complex(0.0, 1.0)

def f(z):
    return one / (z * (z + one))

'''
Integrate the simplified integral in polar coordinates.
'''
def polarIntegral(R):
    N = 100
    dTheta = pi / N
    sum = 0
    for index in range(1, N + 1):
        theta = index * pi / N 
        cosT = cos(theta - (dTheta / 2.0))
        sum += ((R * cosT + one) / (R * R + 2.0 * R * cosT + one))
    return 2.0 * i * sum * dTheta

print "Polar Integral:"
for R in [0.1, 0.5, 0.9, 1.1, 1.5]:
    print "R=" + str(R) + " => " + str(polarIntegral(R))

'''
Integrate directly.
'''
def directIntegral(R):
    N = 100
    dTheta = tao / N
    sum = 0
    for index in range(1, N + 1):
        theta = index * tao / N 
        cosT = cos(theta - (dTheta / 2.0))
        sinT = sin(theta - (dTheta / 2.0))
        dz = R * (-sinT + i * cosT) * dTheta
        z = R * (cosT + i * sinT)
        sum += f(z) * dz
    return sum

print "Direct Integral:"
for R in [0.1, 0.5, 0.9, 1.1, 1.5]:
    print "R=" + str(R) + " => " + str(directIntegral(R))


