'''
Under Construction. This may not work for you. Oct 29, 2013.
'''
from e2ga import *
from symbolic import *

x = Variable("x")
b = Binding("x",3)
print b.name
print b.expr
env = Environment(None, Binding("x", 3))
print env.lookup("x")
print env.evaluate(x)
