from e3ga import *
from math import *

def circumcircle(p1, p2, p3):
    x1 = p2 - p1
    x2 = p3 - p2
    x3 = p1 - p3
    
    x11 = x1.dot(x1)
    x12 = x1.dot(x2)
    x13 = x1.dot(x3)
    x22 = x2.dot(x2)
    x23 = x2.dot(x3)
    x33 = x3.dot(x3)
    
    d = 2 * (x13 * x12 - x11 * x23)
    a1 = (2 * x13 * x12 - x23 * x11 + x12 * x33) / d
    a2 = (x33 * (x12 - x11) - (x13 + x23) * x11) / d
    a3 = x11 * (x13 + x33) / d
    print "a1: %s" % a1
    print "a2: %s" % a2
    print "a3: %s" % a3

#    denom = 0.5 * magnitude((p1-p2).cross(p2-p3)) ** 2    
#    alpha = quadrance(p2-p3) * (p1-p2).dot(p1-p3) / denom
#    beta  = quadrance(p1-p3) * (p2-p1).dot(p1-p3) / denom
#    gamma = quadrance(p1-p2) * (p3-p1).dot(p3-p2) / denom
#    print "alpha: %s" % alpha
#    print "beta:  %s" % beta
#    print "gamma: %s" % gamma
    
    center = (a1 * p1 + a2 * p2 + a3 * p3) / d
#   center = (alpha * p1 + beta * p2 + gamma * p3) / d
    radius = magnitude(p3 - center)
    print "d1: %s" % magnitude(p1 - center)
    print "d2: %s" % magnitude(p2 - center)
    print "d3: %s" % magnitude(p3 - center)
    print "p1: %s" % p1
    print "p2: %s" % p2
    print "p3: %s" % p3
    return {'center':center, 'radius':radius}


p1 = VectorE3( 1.0, 0.0, 0.0)
p2 = VectorE3( 2.0, 1.0, 0.0)
p3 = VectorE3( 1.0, 2.0, 0.0)

cc = circumcircle(p1,p2,p3);

print cc