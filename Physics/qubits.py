'''
Rotors for the cardinal points in 3D space.

Seems to be a problem computing z-. Wrong magnitude.

z+ <-> 1
z- <-> -e31 = - I * e2

x+ <-> (1 - e31)   / sqrt(2)
x- <-> (e23 - e12) / sqrt(2)

y+ <-> (1 - e12 + e23 - e31) / 2
y- <-> (1 + e12 - e23 - e31) / 2

'''
from e3ga import *
from math import exp, sqrt

def rotor(theta, phi):
    return exp(-I * e3 * phi / 2.0) * exp(-I * e2 * theta / 2.0)

def amplitude(phi, psi):
    ihp = ~phi
    ihppsi = ihp * psi
    return (ihppsi)[0] - ((ihppsi * I * e3)[0]) * I * e3

zp = rotor(0.0, 0.0)
zm = rotor(pi,  0.0)

xp = rotor(pi / 2.0, 0.0)
xm = rotor(pi / 2.0, pi)

yp = rotor(pi / 2.0, 1.0 * pi / 2.0)
ym = rotor(pi / 2.0, 3.0 * pi / 2.0)

zp = ScalarE3(1.0)
zm = -I * e2

xp = (ScalarE3(1.0) - e3 * e1) / sqrt(2.0)
xm = (e2 * e3 - e1 * e2) / sqrt(2.0)

yp = (ScalarE3(1.0) - e1 * e2 + e2 * e3 - e3 * e1) / 2.0
ym = (ScalarE3(1.0) + e1 * e2 - e2 * e3 - e3 * e1) / 2.0

print "z+ => " + str(zp)
print "z- => " + str(zm)
print "x+ => " + str(xp)
print "x- => " + str(xm)
print "y+ => " + str(yp)
print "y- => " + str(ym)

# For E3 we can check the eigenvalues by division.
print e3 * zp * e3 / zp
print e3 * zm * e3 / zm

print e1 * xp * e3 / xp
print e1 * xm * e3 / xm

print e2 * yp * e3 / yp
print e2 * ym * e3 / ym

print amplitude(zp, xm)