from e3ga import *
from math import exp

def rotor(theta, phi):
    return exp(-I * e3 * phi / 2) * exp(-I * e2 * theta / 2)

print "|z+> => " + str(rotor(0,0))
print "|z-> => " + str(rotor(pi,0))
print "|x+> => " + str(rotor(pi/2,0))
print "|x-> => " + str(rotor(pi/2,pi))
print "|y+> => " + str(rotor(pi/2,+pi/2))
print "|y-> => " + str(rotor(pi/2,-pi/2))