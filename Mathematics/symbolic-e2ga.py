'''
Under Construction. This may not work for you. Oct 29, 2013.
'''
from e2ga import *
from symbolic import *

i = VectorE2(1, 0)
j = VectorE2(0, 1)

w = Variable("w")
x = Variable("x")
y = Variable("y")
z = Variable("z")
expr = x * i
print expr
b = Binding("x", 2)
print b
env = Environment(None, b)
#print Binding(str(expr), expr.evaluate(env))
