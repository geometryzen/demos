'''
I'm starting here with the representation in which time is the scalar part of a multivector.
It's fascinating to see this work using just the Euclidean2 numbers.
Obviously this requires the invariant interval to be calculated as X * cliffordConjugate(X).
The next steps will be:
1. Perform the same calculation using Spacetime Algebra.
2. Experiment with an arbitrary field. e.g. Rational or Complex (prelude to symbolic calculation).
3. Visualization technigues. Should be able to show and improve upon Spacetime diagrams.
'''
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

Lcc = cliffordConjugate(L)

print "cliffordConjugate(L): " + str(Lcc)

X = ScalarE2(4) + VectorE2(3, 1)

print ""
print "X : " + str(X)
print "ct: " + str(X[0])
print "r : " + str(X[1])
print "Interval : " + str(X * cliffordConjugate(X))

xPrimed = Lcc * X * Lcc

print ""
print "x' : " + str(xPrimed)
print "ct': " + str(xPrimed[0])
print "r' : " + str(xPrimed[1])
print "Interval : " + str(xPrimed * cliffordConjugate(xPrimed))
