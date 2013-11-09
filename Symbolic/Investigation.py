'''
Investigating the feasibility of CAS.
'''
from symbolic import *

a = Variable("a")
b = Variable("b")
c = Variable("c")

tree = a * (b + c)

print tree
print repr(tree)
print a.uuid
print b.uuid
print tree.uuid