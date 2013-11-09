'''
Investigating the feasibility of CAS.
'''
from symbolic import *

# The following functions are provided for testing purposes.
def assertEqual(actual, expect):
    if str(expect) == str(actual):
        pass
    else:
        print {"actual": actual, "expect": expect}

def explain(m):
    print str(m) + " is " + repr(m)
    return m

def showValue(name, m):
    print name + " => " + str(m)
    return m

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

assertEqual(co.execute(a * b), b * a)
assertEqual(dL.execute(a * (b + c)), a * b + a * c)
assertEqual(fL.execute(a * b + a * c), a * (b + c))

print dL.execute(tree)
print fL.execute(dL.execute(tree))

expr = a * (b * c)
print expr
print aL.execute(expr)
print aR.execute(aL.execute(expr))