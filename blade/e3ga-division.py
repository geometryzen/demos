# e3ga-division.py
from eight import *

def explain(m):
    print str(m) + " is " + repr(m)
    return m

def showValue(name, m):
    print name + " => " + str(m)
    return m

zero = explain(Euclidean3(0, 0, 0, 0, 0, 0, 0, 0))
one  = explain(Scalar3(1))
two  = explain(Scalar3(2))
three= explain(3)
e1   = explain(Vector3(1, 0, 0))
e2   = explain(Vector3(0, 1, 0))
e3   = explain(Vector3(0, 0, 1))
e12  = explain(Bivector3(1, 0, 0))
e23  = explain(Bivector3(0, 1, 0))
e31  = explain(Bivector3(0, 0, 1))
I    = explain(Pseudoscalar3(1))

blades = [zero, one, two, three, e1, e2, e3, e12, e23, e31, I]

print one / three

print ""
print "Geometric Product Table *"
print "========================="
for a in blades:
    for b in blades:
        showValue(str(a) + " * " + str(b), a * b)
    print ""
