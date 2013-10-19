from e3ga import *
from math import *

def gamma(beta):
    return 1 / sqrt(1 - beta * beta)

def boost(beta):
    g = gamma(beta)
    return 1 + g + g + beta

beta = VectorE3(3.0/5.0, 0, 0)

print "beta: " + repr(beta)

gamma = gamma(beta)

print "gamma: " + repr(gamma)

L = boost(beta)

print "L: " + repr(L)
