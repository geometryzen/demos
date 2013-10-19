from e2ga import *
from math import *

def gamma(beta):
    return 1 / sqrt(1 - beta * beta)

def boost(beta):
    g = gamma(beta)
    return (1 + g + g * beta) / sqrt(2 * (1 + g))

beta = VectorE2(3.0/5.0, 0.0)

print "beta: " + str(beta)

g = gamma(beta)

print "gamma: " + str(g)

L = boost(beta)

print "L: " + str(L)

x = ScalarE2(4) + VectorE2(3, 1)

print "x : " + str(x)
print "ct: " + str(x[0])
print "r : " + str(x[1])

Lcc = cliffordConjugate(L)

print "cliffordConjugate(L): " + str(Lcc)

xPrimed = Lcc * x * Lcc

print "x': " + str(xPrimed)
