'''
Matrices over a complex field.
'''
from matrix import *
from cmath import *

zero = complex(0.0, 0.0)
one = complex(1.0, 0.0)
i = complex(0.0, 1.0)

M = Matrix2x2(Matrix2x1(zero, one), Matrix2x1(one, zero))

print "M is a 2x2 matrix."
print ""
print "Construction..."
print "repr(M) => " + repr(M)
print ""
print "Notation..."
print "str(M) => " + str(M)
print ""
print "Extraction of the column vectors..."
print "M[0] => " + str(M[0])
print "M[1] => " + str(M[1])
print ""
print "Extraction of the elements of each column vector..."
print "M[0][0] => " + str(M[0][0])
print "M[0][1] => " + str(M[0][1])
print "M[1][0] => " + str(M[1][0])
print "M[1][1] => " + str(M[1][1])
print ""
print "Transposition..."
print "M.transpose() => " + str(M.transpose())
print "M => " + str(M)
