# e2ga-demo.py
# Demonstration of Euclidean 2D Geometric Algebra.
from blade import *

# Convenience functions for creating Blades.
def Scalar(w):
    return Euclidean2(w, 0, 0, 0)

def Vector(x, y):
    return Euclidean2(0, x, y, 0)

def Pseudoscalar(s):
    return Euclidean2(0, 0, 0, s)

def explain(m):
    print str(m) + " is " + repr(m)
    return m

def showValue(name, x):
    print name + " => " + str(x)
    return x

zero = explain(Euclidean2(0,0,0,0))
one  = explain(Scalar(1))
two  = explain(Scalar(2))
i    = explain(Vector(1, 0))
j    = explain(Vector(0, 1))
I    = explain(Pseudoscalar(1))

blades = [one, two, i, j, I]

print ""
print "Sum"
for a in blades:
    print ""
    for b in blades:
        showValue(str(a) + " + " + str(b), a + b)
print ""
print "Difference"
for a in blades:
    print ""
    for b in blades:
        showValue(str(a) + " - " + str(b), a - b)
print ""
print "Geometric Product"
for a in blades:
    print ""
    for b in blades:
        showValue(str(a) + " * " + str(b), a * b)
print ""
print "Exterior Product"
for a in blades:
    print ""
    for b in blades:
        showValue(str(a) + " ^ " + str(b), a ^ b)
print ""
print "Left Contraction"
for a in blades:
    print ""
    for b in blades:
        showValue(str(a) + " << " + str(b), a << b)
print ""
print "Right Contraction"
for a in blades:
    print ""
    for b in blades:
        showValue(str(a) + " >> " + str(b), a >> b)
