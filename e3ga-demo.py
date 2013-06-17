# e3ga-demo.py
# Demonstration of Euclidean 3D Geometric Algebra.
from blade import *

def Scalar(w):
    return Euclidean3(w, 0, 0, 0, 0, 0, 0, 0)

def Vector(x, y, z):
    return Euclidean3(0, x, y, z, 0, 0, 0, 0)

def Bivector(xy, yz, zx):
    return Euclidean3(0, 0, 0, 0, xy, yz, zx, 0)

def Pseudoscalar(s):
    return Euclidean3(0, 0, 0, 0, 0, 0, 0, s)

def explain(m):
    print str(m) + " is " + repr(m)
    return m

def showValue(name, m):
    print name + " => " + str(m)
    return m

zero = explain(Euclidean3(0, 0, 0, 0, 0, 0, 0, 0))
one  = explain(Scalar(1))
e1   = explain(Vector(1, 0, 0))
e2   = explain(Vector(0, 1, 0))
e3   = explain(Vector(0, 0, 1))
e12  = explain(Bivector(1, 0, 0))
e23  = explain(Bivector(0, 1, 0))
e31  = explain(Bivector(0, 0, 1))
I    = explain(Pseudoscalar(1))

blades = [one, e1, e2, e3, e12, e23, e31, I]

# Skulpt bug? The string representation of the list does not recurse.
# print str(blades)

# addition uses the + operator, as you would expect.
sum = showValue("sum", one + e1 + e2 + e3 + e12 + e23 + e31 + I)

# grade extraction is performed using Python's indexing operator [].
print ""
print "Grade extraction operator []"
print "============================"
for grade in range(0, 4):
    showValue("sum[" + str(grade) + "]", sum[grade])

# subtraction uses the - operator, as you would expect.
showValue("zero - sum", zero - sum)
# Skulpt bug? It commutes the arguments!
# showValue("0 - sum", 0 - sum)
print ""
print "Geometric Product Table"
print "======================="
for a in blades:
    for b in blades:
        showValue(str(a) + " * " + str(b), a * b)
    print ""

