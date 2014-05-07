from e2ga import *
from math import *

p1 = VectorE2(1.0, 0.0)
p2 = VectorE2(2.0, 1.0)
p3 = VectorE2(1.0, 2.0)

def circle(p1, p2, p3):
    x1 = p2 - p1
    x2 = p3 - p2
    x3 = p1 - p3
    
    x11 = x1 << x1
    x12 = x1.dot(x2)
    x13 = x1 << x3
    x22 = x2 << x2
    x23 = x2 << x3
    x33 = x3 << x3
    
    d = 2 * (x13 * x12 - x11 * x23)

    a1 = - x22 * x13 / d
    a2 = - x33 * x12 / d
    a3 = - x11 * x23 / d
    
    center = (a1 * p1 + a2 * p2 + a3 * p3)
    radius = magnitude(p3 - center)
    return (center, radius)

c = circle(p1,p2,p3);

center = c[0]
radius = c[1]
print "center: %s" % center
print "radius: %s" % radius
print "|p1-center|: %s" % magnitude(p1-center)
print "|p2-center|: %s" % magnitude(p2-center)
print "|p3-center|: %s" % magnitude(p3-center)
