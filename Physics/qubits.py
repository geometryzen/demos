from e3ga import *
from math import exp

def rotor(theta, phi):
    return exp(-I * e3 * phi / 2) * exp(-I * e2 * theta / 2)

print "|0> => " + str(rotor(0,0))
print "|1> => " + str(rotor(pi,0))
print "|+> => " + str(rotor(pi/2,0))