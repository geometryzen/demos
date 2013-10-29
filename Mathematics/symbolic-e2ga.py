'''
Under Construction. This may not work for you. Oct 29, 2013.
'''
from e2ga import *
from symbolic import *

x = Variable("x")
env = Environment(None, Binding("x", 3))
print x.evaluate(env)
