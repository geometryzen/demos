'''
Matrices over a complex field.
'''
from matrix import *
from cmath import *
from math import *

zero = complex(0.0, 0.0)
one = complex(1.0, 0.0)
i = complex(0.0, 1.0)

I = Matrix2x2(Matrix2x1(one, zero), Matrix2x1(zero, one))
X = Matrix2x2(Matrix2x1(zero, one), Matrix2x1(one, zero))
Y = Matrix2x2(Matrix2x1(zero, i), Matrix2x1(-i, zero))
Z = Matrix2x2(Matrix2x1(one, zero), Matrix2x1(zero, -one))
H = (X + Z) * sqrt1_2

print "I => " + str(I)
print "X => " + str(X)
print "Y => " + str(Y)
print "Z => " + str(Z)
print "H => " + str(H)
