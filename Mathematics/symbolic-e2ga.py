'''
Under Construction. This may not work for you. Oct 29, 2013.
'''
from e2ga import *
from symbolic import *

i = VectorE2(1,0)

x = Variable("x")
expr = x * x + 2
b = Binding("x", i)
print b
env = Environment(None, b)
print Binding(str(expr), expr.evaluate(env))
