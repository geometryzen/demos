'''
Support for 2x2, 2x1, 1x2 matrices over an arbitrary field.
Under Construction. Nov 17, 2013.
'''
from matrix import *
from math import *
from cmath import *

zp = Matrix2x1(complex(1.0, 0.0), complex(0.0, 0.0))
zm = Matrix2x1(complex(0.0, 0.0), complex(1.0, 0.0))

print "zp[0] => " + str(zp[0])
print "zp[1] => " + str(zp[1])

hxp = (zp + zm) / sqrt(2.0)
hxm = (zp - zm) / sqrt(2.0)

print "|0> => \n" + str(zp) 
print "|1> => \n" + str(zm) 
print "|+> => \n" + str(hxp) 
print "|-> => \n" + str(hxm)

H = Matrix2x2(zp, zm)

print H
print repr(H)
