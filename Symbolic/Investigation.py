'''
Investigating the feasibility of CAS.
'''
from symbolic import *

a = Variable("a")
b = Variable("b")
c = Variable("c")

tree = a + b - c

walker = TreeWalker(tree)

print tree
