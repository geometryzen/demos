'''
Investigation into improving accuracy in the use of trigonometric functions.
'''
from math import *
from e3ga import Euclidean3, I, e3, e2

def rotor(theta, phi):
    R2 = exp(-I * e3 * phi / 2.0)
    R1 = exp(-I * e2 * theta / 2.0)
    return R1
    #return R2 * R1

print "sqrt(2) => " + str(sqrt(2))
print e
print pi
print tao
print cos(pi / 4.0)
print sin(pi / 4.0)
print sqrt1_2
print sqrt2
print sqrt2 * sqrt2
print sqrt1_2 * sqrt1_2
print cos(pi / 4.0) * cos(pi / 4)

print cos((pi / 2.0) / 2.0)
print sin((pi / 2.0) / 2.0)
print exp((pi / 2.0) / 2.0)

print rotor(pi / 2.0, 0.0)
print (I * e2 * (pi / 2.0)).quaternion.y
print -pi / 2
