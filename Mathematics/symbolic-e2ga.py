'''
Under Construction. This may not work for you. Oct 29, 2013.
'''
from e2ga import *
from symbolic import *

x = Variable("x")
y = Variable("y")
z = x + 2
print z
env = Environment()
binding = Binding("x", 3)
print binding
print env
print env.evaluate(z)

p = PointE2(x, y)
print p
print repr(p)
A = PointE2(2, 3)
B = PointE2(5, 2)
print A
print B
