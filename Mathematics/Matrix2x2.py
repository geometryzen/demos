'''
Support for 2x2, 2x1, 1x2 matrices over an arbitrary field.
Under Construction. Nov 17, 2013.
'''
from matrix import *
from cmath import *

hxp = Matrix2x1(complex(1,0), complex(0,1)) / sqrt(2.0)

print hxp
print repr(hxp)
