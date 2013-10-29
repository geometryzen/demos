'''
Under Construction. This may not work for you. Oct 29, 2013.
'''
from symbolic import *

w = Variable("w")
x = Variable("x")
y = Variable("y")
s = Variable("s")

A = PointE2(x, y)
B = PointE2(5, 2)
print Binding("A", A)
print Binding("B", B)
#print p.x
#print p.y

expr = x + 1
env = Environment() + Binding("w", 1.0) + Binding("x", 2) + Binding("y", 3) + Binding("s", 4)
print Binding(str(expr), expr.evaluate(env))
