'''
Matrices over a complex field.

The conjugate of a real number is simply the real number.
The conjugate of a complex number is the number reflected in the x-axis.
The conjugate of a matrix of elements is the matrix of the conjugated elements.
This could be extended to Quaternions, Octonions (division algebras) as well as the Clifford Conjugate of multivectors.
'''
from matrix import *
from cmath import *
from math import *

print "conjugate(1) => " + str(conjugate(1))

zero = complex(0.0, 0.0)
one = complex(1.0, 0.0)
i = complex(0.0, 1.0)

print "conjugate(zero) => " + str(conjugate(zero))
print "conjugate(one) => " + str(conjugate(one))
print "conjugate(i) => " + str(conjugate(i))

print "4+3i => " + str(4+3*i)
print "conjugate(4+3i) => " + str(conjugate(4+3*i))

I = Matrix2x2(Matrix2x1(1, 0), Matrix2x1(0, 1))
X = Matrix2x2(Matrix2x1(zero, one), Matrix2x1(one, zero))
Y = Matrix2x2(Matrix2x1(zero, i), Matrix2x1(-i, zero))
Z = Matrix2x2(Matrix2x1(one, zero), Matrix2x1(zero, -one))
H = (X + Z) * sqrt1_2

print "I => " + str(I)
print "X => " + str(X)
print "Y => " + str(Y)
print "Z => " + str(Z)
print "H => " + str(H)

print "conjugate(Y[0]) => " + str(conjugate(Y[0]))
print "conjugate(Y[1].transpose()) => " + str(conjugate(Y[1].transpose()))
print repr(I)
print "conjugate(I) => " + str(conjugate(I))
print "conjugate(X) => " + str(conjugate(X))
print "conjugate(Y) => " + str(conjugate(Y))
print "conjugate(Z) => " + str(conjugate(Z))
