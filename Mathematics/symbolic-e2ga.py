'''
Under Construction. This may not work for you. Oct 29, 2013.
'''
from e2ga import *
from symbolic import *

x = Variable("x")
expr = x * x
b = Binding("x", 2)
print b
env = Environment(None, b)
print Binding(str(expr), expr.evaluate(env))
