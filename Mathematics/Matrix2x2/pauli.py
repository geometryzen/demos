'''
Support for 2x2, 2x1, 1x2 matrices over an arbitrary field.
Under Construction. Nov 19, 2013.

I'm going to have the use-case that 2x2 matrix algebra should support
a course in Quantum Mechanics. So I will be interested in how well the
library can support the learning of Linear Algebra using matrices as
the representation over a complex field. This is the traditional "Dirac" approach.
It should be possible to work in both the state vector and density operator formalism.

Of course, I'll want to represent qubits as spinors in Geometric Algebra
as well. The challenge there will be library programming for multiparticle states.
'''
from matrix import *
from math import *
from cmath import *

i = complex(0.0, 1.0)

I = Matrix2x2(Matrix2x1(1, 0), Matrix2x1(0, 1))
X = Matrix2x2(Matrix2x1(0, 1), Matrix2x1(1, 0))
Y = Matrix2x2(Matrix2x1(0, i), Matrix2x1(-i, 0))
Z = Matrix2x2(Matrix2x1(1, 0), Matrix2x1(0, -1))



