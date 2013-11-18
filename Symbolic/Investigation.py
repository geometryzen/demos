'''
Investigating the feasibility of CAS.
'''
from symbolic import *
from matrix import *

# The following functions are provided for testing purposes.
def assertEqual(fn, actual, expect):
    if str(fn.execute(actual)) == str(expect):
        print str(actual) + " => " + str(fn.execute(actual)) + " (" + str(fn) + ")"
        pass
    else:
        print {"fn": fn, "output": str(fn.execute(actual)), "expect": str(expect), "input": str(actual)}

def explain(m):
    print str(m) + " is " + repr(m)
    return m

def showValue(name, m):
    print name + " => " + str(m)
    return m

a = Variable("a")
b = Variable("b")
c = Variable("c")
d = Variable("d")

print "The Basic tree transformations: Distribution, Factorization, Association, and Commutation."
assertEqual(DistribL(), a * (b + c)   , (a * b) + (a * c) )
assertEqual(DistribR(), (a + b) * c   , (a * c) + (b * c) )

assertEqual(FactorL(),  (a * b) + (a * c) , a * (b + c)   )
assertEqual(FactorR(),  (a * b) + (c * b) , (a + c) * b   )

assertEqual(AssocL(),   a * (b * c)   , (a * b) * c       )
assertEqual(AssocR(),   (a * b) * c   , a * (b * c)       )

assertEqual(Commute(),  a * b         , b * a             )

M = Matrix2x2(Matrix2x1(a,c),Matrix2x1(b,d))
print M
