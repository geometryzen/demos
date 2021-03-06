'''
I'm starting here with the representation in which time is the scalar part of a multivector.
It's fascinating to see this work using just the Euclidean2 numbers - no Lorentzian metric yet but still geometric.
Obviously this requires the invariant interval to be calculated as X * cliffordConjugate(X).
It does demonstrate the Geometric Algebra approach and a Geometric (coordinate-free) calculation.

The next steps will be:
1. Perform the same calculation using Spacetime Algebra.
2. Experiment with an arbitrary field. e.g. Rational or Complex (prelude to symbolic calculation and accurate calculation).
3. Visualization techniques. Should be able to show and improve upon Spacetime diagrams.

References... 
Hestenes: New Foundations for Classical Mechanics
Bondi: Relativity and Common Sense
'''
from e2ga import *
from math import *

def gamma(beta):
    return 1 / sqrt(1 - beta * beta)

def boost(beta):
    g = gamma(beta)
    return (1 + g + g * beta) / sqrt(2 * (1 + g))

# TODO: Complete - get rid of those square roots and make it an entirely Rational field.
# TODO: I wonder if the direction can be incorporated with k into something geometric?
def boostSquared(k, direction):
    g = gamma(beta)
    return (1 + g + g * beta) / sqrt(2 * (1 + g))

k = ScalarE2(2.0)

print "k: " + str(k)

B = (k * k - 1) / (k * k + 1)

i = VectorE2(1, 0)

beta = B * i

print "beta: " + str(beta)

g = gamma(beta)

print "gamma: " + str(g)

L = boost(beta)

print ""
print "L: " + str(L)

Lcc = cliffordConjugate(L)

print "cliffordConjugate(L): " + str(Lcc)

print "L * cliffordConjugate(L): " + str(L * Lcc)

X = ScalarE2(4) + VectorE2(3, 1)

print ""
print "X : " + str(X)
print "ct: " + str(X[0])
print "r : " + str(X[1])
print "Interval Quadrance : " + str(X * cliffordConjugate(X))

xPrimed = Lcc * X * Lcc

print ""
print "X' : " + str(xPrimed)
print "ct': " + str(xPrimed[0])
print "r' : " + str(xPrimed[1])
print "Interval Quadrance : " + str(xPrimed * cliffordConjugate(xPrimed))
