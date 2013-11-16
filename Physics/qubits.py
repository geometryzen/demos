'''
Rotors for the cardinal points in 3D space.

Seems to be a problem computing z-

z+ <-> 1
z- <-> -e31 = - I * e2

x+ <-> (1 - e31) / sqrt(2)
x- <->

'''
from e3ga import *
from math import exp

def rotor(theta, phi):
    return exp(-I * e3 * phi / 2.0) * exp(-I * e2 * theta / 2.0)

print "|z+> => " + str(rotor(0.0,       0.0))
print "|z-> => " + str(rotor(pi,        0.0))
print "|x+> => " + str(rotor(pi / 2.0,  0.0))
print "|x-> => " + str(rotor(pi / 2.0,  pi))
print "|y+> => " + str(rotor(pi / 2.0, +pi / 2.0))
print "|y-> => " + str(rotor(pi / 2.0, -pi / 2.0))