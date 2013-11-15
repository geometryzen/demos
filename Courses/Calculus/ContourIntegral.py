'''
Experiment with the calculation and visualization of a path integral in the complex plane.

f(z) = 1/(z(z+1)), where the contour is a circle: |z| = R > 1.

We can convert this to polar coordinates and simplify.
We can also chug through the integral using Cartesian coordinates.

'''
from cmath import *
from math import cos, sin

def f(z):
    return one / (z * (z + 1))

'''
Integrate the simplified integral in polar coordinates.
'''
def polarIntegral(R):
    N = 20
    dTheta = tao / N
    sum = 0
    for index in range(1, N + 1):
        theta = index * tao / N 
        cosT = cos(theta)
        sum += ((R * cosT + one) / (R * R + 2 * R * cosT + one))
    return sum * dTheta * complex(0.0, 1.0)

print "Polar Integral:"
for r in range(0, 20):
    R = r / 10.0
    print "R=" + str(R) + " => " + str(polarIntegral(R))

'''
Integrate directly.
'''
def directIntegral(R):
    N = 20
    dTheta = tao / N
    sum = 0
    for index in range(1, N + 1):
        theta = index * tao / N 
        cosT = cos(theta)
        sinT = sin(theta)
        dz = R * (-sinT + i * cosT) * dTheta
        z = R * (cosT + i * sinT)
        sum += f(z) * dz
    return sum

print "Direct Integral:"
for r in range(0, 20):
    R = r / 10.0
    print "R=" + str(R) + " => " + str(directIntegral(R))


