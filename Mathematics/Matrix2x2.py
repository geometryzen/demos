'''
Support for 2x2, 2x1, 1x2 matrices over an arbitrary field.
Under Construction. Nov 18, 2013.
'''
from matrix import *
from math import *
from cmath import *
from symbolic import *

zero = complex(0.0, 0.0)
one = complex(1.0, 0.0)
i = complex(0.0, 1.0)

zp = Matrix2x1(one, zero)
zm = Matrix2x1(zero, one)

I = Matrix2x2(zp, zm)
print "The Identity Matrix, I"
print I

X = Matrix2x2(zm, zp)
print "The Pauli X"
print X

Y = Matrix2x2(Matrix2x1(zero, i), Matrix2x1(-i, zero))
print "The Pauli Y"
print Y

Z = Matrix2x2(Matrix2x1(one, zero), Matrix2x1(zero, -one))
print "The Pauli Z"
print Z

print "-i * X * Y"
print -i * X * Y


print "zp[0] => " + str(zp[0])
print "zp[1] => " + str(zp[1])

hxp = (zp + zm) / sqrt(2.0)
hxm = (zp - zm) / sqrt(2.0)

print "|0> => \n" + str(zp) 
print "|1> => \n" + str(zm) 
print "|+> => \n" + str(hxp) 
print "|-> => \n" + str(hxm)

H = Matrix2x2(hxp, hxm)
print "H[0][0] => " + str(H[0][0])
print "H[0][1] => " + str(H[0][1])
print "H[1][0] => " + str(H[1][0])
print "H[1][1] => " + str(H[1][1])



