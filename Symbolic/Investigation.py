'''
Investigating the feasibility of CAS.
'''
from symbolic import *

a = Variable("a")
b = Variable("b")
c = Variable("c")

tree = a * (b + c)

walker = TreeWalker(tree)

dL = DistribL()
fL = FactorL()
aL = AssocL()

print tree
print dL.execute(tree)
print fL.execute(dL.execute(tree))