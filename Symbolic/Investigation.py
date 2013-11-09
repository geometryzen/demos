'''
Investigating the feasibility of CAS.
'''
from symbolic import *

a = Variable("a")
b = Variable("b")
c = Variable("c")

tree = a * (b + c)

walker = TreeWalker(tree)
print walker.contextNode
print walker.ancestorAxis
if walker.moveToFirstChild():
    print walker.contextNode
else:
    print "cannot move to first child of " + str(walker.contextNode)