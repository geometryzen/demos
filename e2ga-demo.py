# e2ga-demo.py
from blade import *

# Convenience functions for creating Blades.
def Scalar(w):
    return Euclidean2(w, 0, 0, 0)

def Vector(x, y):
    return Euclidean2(0, x, y, 0)

def Pseudoscalar(s):
    return Euclidean2(0, 0, 0, s)

def explain(m):
    print str(m) + " is " + repr(m)
    return m

def showValue(name, m):
    print name + " => " + str(m)
    return m

one = explain(Scalar(1))
print "str(one): " + str(one)
print "repr(one): " + repr(one)

i = Vector(1, 0)
print "str(i): " + str(i)
print "repr(i): " + repr(i)

j = Vector(0, 1)
print "str(j): " + str(j)
print "repr(j): " + repr(j)

I = Pseudoscalar(1)
print "str(ij): " + str(I)
print "repr(ij): " + repr(I)

print "one + i + j + I = " + str(one + i + j + I)
print ""
print "Geometric Product"
print "1 * 1 = " + str(one * one)
print "1 * i = " + str(one * i)
print "1 * j = " + str(one * j)
print "1 * I = " + str(one * I)
print ""
print "i * 1 = " + str(i * one)
print "i * i = " + str(i * i)
print "i * j = " + str(i * j)
print "i * I = " + str(i * I)
print ""
print "j * 1 = " + str(j * one)
print "j * i = " + str(j * i)
print "j * j = " + str(j * j)
print "j * I = " + str(j * I)
print ""
print "I * 1 = " + str(I * one)
print "I * i = " + str(I * i)
print "I * j = " + str(I * j)
print "I * I = " + str(I * I)
print ""
print "Exterior Product"
print "1 ^ 1 = " + str(one ^ one)
print "1 ^ i = " + str(one ^ i)
print "1 ^ j = " + str(one ^ j)
print "1 ^ I = " + str(one ^ I)
print ""
print "i ^ 1 = " + str(i ^ one)
print "i ^ i = " + str(i ^ i)
print "i ^ j = " + str(i ^ j)
print "i ^ I = " + str(i ^ I)
print ""
print "j ^ 1 = " + str(j ^ one)
print "j ^ i = " + str(j ^ i)
print "j ^ j = " + str(j ^ j)
print "j ^ I = " + str(j ^ I)
print ""
print "I ^ 1 = " + str(I ^ one)
print "I ^ i = " + str(I ^ i)
print "I ^ j = " + str(I ^ j)
print "I ^ I = " + str(I ^ I)
print ""
print "Left Contraction"
print "1 << 1 = " + str(one << one)
print "1 << i = " + str(one << i)
print "1 << j = " + str(one << j)
print "1 << I = " + str(one << I)
print ""
print "i << 1 = " + str(i << one)
print "i << i = " + str(i << i)
print "i << j = " + str(i << j)
print "i << I = " + str(i << I)
print ""
print "j << 1 = " + str(j << one)
print "j << i = " + str(j << i)
print "j << j = " + str(j << j)
print "j << I = " + str(j << I)
print ""
print "I << 1 = " + str(I << one)
print "I << i = " + str(I << i)
print "I << j = " + str(I << j)
print "I << I = " + str(I << I)
print ""
print "Right Contraction"
print "1 >> 1 = " + str(one >> one)
print "1 >> i = " + str(one >> i)
print "1 >> j = " + str(one >> j)
print "1 >> I = " + str(one >> I)
print ""
print "i >> 1 = " + str(i >> one)
print "i >> i = " + str(i >> i)
print "i >> j = " + str(i >> j)
print "i >> I = " + str(i >> I)
print ""
print "j >> 1 = " + str(j >> one)
print "j >> i = " + str(j >> i)
print "j >> j = " + str(j >> j)
print "j >> I = " + str(j >> I)
print ""
print "I >> 1 = " + str(I >> one)
print "I >> i = " + str(I >> i)
print "I >> j = " + str(I >> j)
print "I >> I = " + str(I >> I)
print ""
print "0.5 * (one + i + j + I) = " + str(0.5 * (one + i + j + I))
