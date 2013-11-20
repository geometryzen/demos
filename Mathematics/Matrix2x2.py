'''
Support for 2x2, 2x1, 1x2 matrices over an arbitrary field.
Under Construction. Nov 19, 2013.

I'm going to have the use-case that 2x2 matrix algebra should support
a course in Quantum Mechanics. So I will be interested in how well the
library can support the learning of Linear Algebra using matrices as
the representation over a complex field. This is the traditional "Dirac" approach.
It should be possible to work in both the state vector and density operator formalism.

Of course, I'll want to represent qubits as spinors in Geometric Algebra
as well.
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

hp = Matrix2x1(one, sqrt2 - one) / (2 * sqrt(1 - sqrt1_2))
hm = Matrix2x1(one, -(sqrt2 + one)) / (2 * sqrt(1 + sqrt1_2))

print hp[0]*hp[0] + hp[1]*hp[1]
print hm[0]*hm[0] + hm[1]*hm[1]

print repr(H * hp)
print repr(H * hm * -1)



