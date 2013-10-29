'''
Under Construction. This may not work for you. Oct 29, 2013.
'''
from e2ga import *
from symbolic import *

i = VectorE2(1, 0)
j = VectorE2(0, 1)

x = Variable("x")
expr = x * i
print expr
b = Binding("x", 2)
print b
env = Environment(None, b)
print Binding(str(expr), expr.evaluate(env))
