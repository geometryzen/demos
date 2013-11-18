'''
Support for 2x2, 2x1, 1x2 matrices over an arbitrary field.
Under Construction. Nov 17, 2013.
'''
from matrix import *
from math import *
from cmath import *

zp = Matrix2x1(complex(1.0, 0.0), complex(0.0, 0.0))
zm = Matrix2x1(complex(0.0, 0.0), complex(1.0, 0.0))

hxp = Matrix2x1(complex(1.0, 0.0), complex(0.0, 1.0)) / sqrt(2.0)

print "|0> => " + str(zp) 
print hxp
print repr(hxp)
