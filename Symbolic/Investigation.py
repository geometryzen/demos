'''
Investigating the feasibility of CAS.
'''
from symbolic import *

# The following functions are provided for testing purposes.
def assertEqual(fn, actual, expect):
    if str(fn.execute(actual)) == str(expect):
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

assertEqual(Commute(), a * b, b * a)
assertEqual(DistribL(), a * (b + c), a * b + a * c)
assertEqual(fL.execute(a * b + a * c), a * (b + c))
assertEqual(aL.execute(a * b + a * c), a * (b + c))
