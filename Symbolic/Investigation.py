'''
Investigating the feasibility of CAS.
'''
from symbolic import *

# The following functions are provided for testing purposes.
def assertEqual(fn, actual, expect):
    if str(fn.execute(actual)) == str(expect):
        pass
    else:
        print {"fn": fn, "actual": str(actual), "expect": str(expect)}

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

assertEqual(Commute(),  a * b         , b * a         )
assertEqual(DistribL(), a * (b + c)   , a * b + a * c )
assertEqual(FactorL(),  a * b + a * c , a * (b + c)   )
assertEqual(AssocL(),   a * (b * c)   , (a * b) * c   )
assertEqual(AssocR(),   (a * b) * c   , a * (b * c)   )
