from e3ga import *

def gamma(beta):
    return (1 + beta * beta)

def boost(velocity):
    return velocity

beta = VectorE3(3.0/5.0, 0, 0)

print "beta: " + str(beta)

gamma = gamma(beta)

print "gamma: " + str(beta)
