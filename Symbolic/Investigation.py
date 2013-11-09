'''
Investigating the feasibility of CAS.
'''
from symbolic import *

a = Variable("a")
b = Variable("b")
c = Variable("c")

tree = a * (b + c)

walker = TreeWalker(tree)

co = Commute()
dL = DistribL()
fL = FactorL()
aL = AssocL()
aR = AssocR()

print tree
print dL.execute(tree)
print fL.execute(dL.execute(tree))

expr = a * (b * c)
print expr
print aL.execute(expr)
print aR.execute(aL.execute(expr))