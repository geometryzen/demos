'''
Support for 2x2, 2x1, 1x2 matrices over an arbitrary field.
Under Construction. Nov 18, 2013.
'''
from matrix import *
from math import *
from cmath import *

zp = Matrix2x1(complex(1.0, 0.0), complex(0.0, 0.0))
zm = Matrix2x1(complex(0.0, 0.0), complex(1.0, 0.0))

I = Matrix2x2(zp, zm)
print "The Identity Matrix, I"
print I

sx = Matrix2x2(zm, zp)
print "The Pauli sigma x"
print sx

sy = Matrix2x2(Matrix2x1(complex(1.0, 0.0), complex(0.0, 1.0)), Matrix2x1(complex(0.0, -1.0), complex(0.0, 0.0)))
print "The Pauli sigma y"
print sy

sz = Matrix2x2(Matrix2x1(complex(1.0, 0.0), complex(0.0, 0.0)), Matrix2x1(complex(0.0, 0.0), complex(0.0, -1.0)))
print "The Pauli sigma z"
print sz

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



