'''
Matrix2x2 used to represent single-qubit operators and spinors.
'''
from matrix import *
from math import *
from cmath import *
from random import *

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
print ""
print "H => " + str(H)
print "H * H => " + str(H * H)

s = Matrix2x1(complex(random(),random()), complex(random(),random()))
s = s / sqrt(abs(conjugate(s.transpose()) * s))
print ""
print "s     => " + str(s)
print "X * s => " + str(X * s)
print ""
print "s     => " + str(s)
print "Z * s => " + str(Z * s)
print ""
print "s     => " + str(s)
Hs = H * s
print "H * s => " + str(H * s)
print "H * H * s => " + str(H * H * s)



