'''
Matrix2x2 used to represent single-qubit operators and spinors.
'''
from matrix import *
from math import *
from cmath import *
from random import *

i = complex(0.0, 1.0)

I = Matrix2x2(Matrix2x1(1.0, 0.0), Matrix2x1(0.0, 1.0))
X = Matrix2x2(Matrix2x1(0, 1), Matrix2x1(1, 0))
Y = Matrix2x2(Matrix2x1(0, i), Matrix2x1(-i, 0))
Z = Matrix2x2(Matrix2x1(1, 0), Matrix2x1(0, -1))

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
print s
#print X * s



