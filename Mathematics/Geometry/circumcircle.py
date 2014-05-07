from e2ga import *

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
    a1 = 2 * x13 * x12 - x23 * x11 + x12 * x33
    return (a1 * p1) / d


p1 = VectorE2(+1, 0)
p2 = VectorE2( 0,+1)
p3 = VectorE2(-1, 0)

print circumcircle(p1,p2,p3);