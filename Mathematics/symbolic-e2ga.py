'''
Under Construction. This may not work for you. Oct 29, 2013.
'''
from e2ga import *
from symbolic import *

x = Variable("x")
y = Variable("y")
sum = Add(x, y)
print repr(x)

p = PointE2(x, y)
print p
print repr(p)
A = PointE2(2, 3)
B = PointE2(5, 2)
print A
print B
