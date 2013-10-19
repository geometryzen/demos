from e2ga import *
from math import *

def gamma(beta):
    return 1 / sqrt(1 - beta * beta)

def boost(beta):
    g = gamma(beta)
    return (1 + g + g * beta) / sqrt(2 * (1 + g))

def LccSquared(k, direction):
    return (k * k + 1) * (1 - direction) / (2 * k)

k = ScalarE2(2.0)

print "k: " + str(k)

B = (k * k - 1) / (k * k + 1)

i = VectorE2(1, 0)

beta = B * i

print "beta: " + str(beta)

g = gamma(beta)

print "gamma: " + str(g)

Lcc2 = LccSquared(k, i)

print ""
print "Lcc2: " + str(Lcc2)

L = boost(beta)

Lcc = cliffordConjugate(L)

print "cliffordConjugate(L): " + str(Lcc)

print "L * cliffordConjugate(L): " + str(L * Lcc)

print "Lcc * Lcc: " + str(Lcc * Lcc)

X = ScalarE2(4) + VectorE2(3, 1)
XPerp = VectorE2(3, 0)

print ""
print "X : " + str(X)
print "ct: " + str(X[0])
print "r : " + str(X[1])
print "Interval Quadrance : " + str(X * cliffordConjugate(X))

xPrimed = Lcc * X * Lcc
xPrimed = Lcc2 * (X - XPerp) + XPerp

print ""
print "X' : " + str(xPrimed)
print "ct': " + str(xPrimed[0])
print "r' : " + str(xPrimed[1])
print "Interval Quadrance : " + str(xPrimed * cliffordConjugate(xPrimed))
