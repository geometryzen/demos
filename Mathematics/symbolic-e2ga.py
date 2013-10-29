'''
Under Construction. This may not work for you. Oct 29, 2013.
'''
from e2ga import *
from symbolic import *

x = Variable("x")
expr = x + int(2)
env = Environment(None, Binding("x", int(2))
print Binding(str(expr), expr.evaluate(env))
