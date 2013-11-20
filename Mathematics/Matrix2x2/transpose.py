from matrix import *
from symbolic import *

a = Variable("a")
b = Variable("b")
c = Variable("c")
d = Variable("d")

M = Matrix2x2(Matrix2x1(a,c), Matrix2x1(b,d))

print "M:"
print repr(M)
print M
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