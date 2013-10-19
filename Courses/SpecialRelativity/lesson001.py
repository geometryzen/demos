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

X = ScalarE2(4) + VectorE2(3, 1)

print "X : " + str(X)
print "ct: " + str(X[0])
print "r : " + str(X[1])

Lcc = cliffordConjugate(L)

print "cliffordConjugate(L): " + str(Lcc)

xPrimed = Lcc * X * Lcc

print "x' : " + str(xPrimed)
print "ct': " + str(xPrimed[0])
print "r' : " + str(xPrimed[1])
