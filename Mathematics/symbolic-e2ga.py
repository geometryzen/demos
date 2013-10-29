'''
Under Construction. This may not work for you. Oct 29, 2013.
'''
from e2ga import *
from symbolic import *

x = Variable("x")
y = 2
expr = x + y
env = Environment(None, Binding("x", 4))
print Binding(str(expr), expr.evaluate(env))
