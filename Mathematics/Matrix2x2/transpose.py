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
print "M.transpose() => " + str(M.transpose())
print M
print M.transpose()
print M.transpose().transpose()
print ""
print "M[0]:"
print M[0]
print ""
print "M[1]:"
print M[1]

s = Matrix2x1(a,b)
print repr(s)
print s
t = Matrix1x2(c,d)
print repr(t)
print t
print t.transpose()
print t.transpose().transpose()