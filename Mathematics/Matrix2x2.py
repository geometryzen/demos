'''
Support for 2x2, 2x1, 1x2 matrices over an arbitrary field.
Under Construction. Nov 17, 2013.
'''
from matrix import *
from math import *
from cmath import *

zp = Matrix2x1(complex(1.0, 0.0), complex(0.0, 0.0))
zm = Matrix2x1(complex(0.0, 0.0), complex(1.0, 0.0))

hxp = (zp + zm)

print "|0> => \n" + str(zp) 
print "|1> => \n" + str(zm) 
print hxp
print repr(hxp)
