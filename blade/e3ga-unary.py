# e3ga-unary.py
from blade import *

def Scalar3(w):
    return Euclidean3(w, 0, 0, 0, 0, 0, 0, 0)    

def Vector3(x, y, z):
    return Euclidean3(0, x, y, z, 0, 0, 0, 0)    

def Bivector3(xy, yz, zx):
    return Euclidean3(0, 0, 0, 0, xy, yz, zx, 0)    

def Pseudoscalar3(xyz):
    return Euclidean3(0, 0, 0, 0, 0, 0, 0, xyz)    

def explain(m):
    print str(m) + " is " + repr(m)
    return m

def showValue(name, m):
    print name + " => " + str(m)
    return m

zero  = explain(Scalar3(0))
one   = explain(Scalar3(1))
two   = explain(Scalar3(2))
three = explain(3)
i     = explain(Vector3(1, 0, 0))
j     = explain(Vector3(0, 1, 0))
k     = explain(Vector3(0, 0, 1))
ij    = explain(Bivector3(1, 0, 0))
jk    = explain(Bivector3(0, 1, 0))
ki    = explain(Bivector3(0, 0, 1))
I     = explain(Pseudoscalar3(1))

showValue("+zero", +zero)
showValue("-zero", +zero)
showValue("~zero", +zero)
showValue("+i", +i)
showValue("-i", -i)
showValue("~i", ~i)
showValue("+ij", +ij)
showValue("-ij", -ij)
showValue("~ij", ~ij)
showValue("+I", +I)
showValue("-I", -I)
showValue("~I", ~I)