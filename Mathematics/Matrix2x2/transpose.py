from matrix import *
from symbolic import *

a = Variable("a")
b = Variable("b")
c = Variable("c")
d = Variable("d")

M = Matrix2x2(Matrix2x1(1,3), Matrix2x1(2,4))

print "M is a 2x2 matrix."
print "repr(M) => " + repr(M)
print "str(M) => " + str(M)
print "M[0] => " + str(M[0])
print "M[1] => " + str(M[1])
print "M[0][0] => " + str(M[0][0])
print "M[0][1] => " + str(M[0][1])
print "M.transpose() => " + str(M.transpose())
print "M => " + str(M)
