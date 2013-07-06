from e2ga import *
from math import random, floor

def showValue(name, m):
    print name + " => " + str(m)
    return m

def ri():
    return floor(100*random())

# In e2ga, both grade involution and Clifford conjugation work in this context.
# Maybe one is more general?
def cliffordConjugate(A):
    return Euclidean2(A.w, -A.x, -A.y, -A.xy)

def gradeInvolution(A):
    return Euclidean2(A.w, -A.x, -A.y, A.xy)

def inverse(M):
    r = ~M
    m = M * r
    s = r * cliffordConjugate(m)
    k = (M * s).w
    return Euclidean2(s.w/k, s.x/k, s.y/k, s.xy/k)

A = Euclidean2(ri(),ri(),ri(),ri())

showValue("A", A)

showValue("1/A", Euclidean2(1,0,0,0)/A)

showValue("inverse(A)", inverse(A))

showValue("A * inverse(A)", A * inverse(A))
