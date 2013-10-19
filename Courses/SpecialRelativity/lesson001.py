from e2ga import *
from math import *

def gamma(beta):
    return 1 / sqrt(1 - beta * beta)

def boost(beta):
    g = gamma(beta)
    return (1 + g + g * beta) / sqrt(2 * (1 + g))

beta = VectorE2(3.0/5.0, 0)

print "beta: " + repr(beta)

g = gamma(beta)

print "gamma: " + repr(g)

L = boost(beta)

print "L: " + str(L)

x = ScalarE2(4) + VectorE2(3, 1)

print "x: " + str(x)

Lcc = cliffordConjugate(L)

xPrimed = Lcc * x * Lcc

print "x': " + repr(xPrimed)
