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
X = Matrix2x2(zm, zp)
Y = Matrix2x2(Matrix2x1(zero, i), Matrix2x1(-i, zero))
Z = Matrix2x2(Matrix2x1(one, zero), Matrix2x1(zero, -one))

hxp = (zp + zm) / sqrt(2.0)
hxm = (zp - zm) / sqrt(2.0)

H = Matrix2x2(hxp, hxm)

hp = Matrix2x1(one, sqrt2 - one)
hm = Matrix2x1(one, -(sqrt2 + one))
print repr(hp)
print repr(hm)

print H
print repr(H * hp)
print repr(H * hm * -1)



