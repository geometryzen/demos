'''
Under Construction. This may not work for you. Oct 29, 2013.
'''
from e2ga import *
from symbolic import *

i = VectorE2(1,0)

x = Variable("x")
expr = i * x
b = Binding("x", 2)
print b
env = Environment(None, b)
print Binding(str(expr), expr.evaluate(env))
