from e2ga import *
from math import floor
from random import random

def showValue(name, m):
    print name + " => " + str(m)
    return m

def ri():
    return floor(100*random())

def cliffordConjugate(A):
    return Euclidean2(A.w, -A.x, -A.y, -A.xy)

def gradeInvolution(A):
    return Euclidean2(A.w, -A.x, -A.y, A.xy)

def inverse(M):
    r = ~M
    s = r * cliffordConjugate(M * r)
    return s / (M * s)[0]

A = Euclidean2(ri(),ri(),ri(),ri())

showValue("A", A)
showValue("A/2", A/2)

showValue("1/A", Euclidean2(1,0,0,0)/A)
showValue("1/A", 1/A)

showValue("inverse(A)", inverse(A))

showValue("A * inverse(A)", A * inverse(A))

B = Euclidean2(2,2,2,2)
showValue("B", B)
B /= 2
showValue("B", B)


