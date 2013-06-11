# e2ga.py
from e2ga import *

one = Scalar2(1)
print "str(one): " + str(one)
print "repr(one): " + repr(one)

i = Vector2(1, 0)
print "str(i): " + str(i)
print "repr(i): " + repr(i)

j = Vector2(0, 1)
print "str(j): " + str(j)
print "repr(j): " + repr(j)

I = Pseudoscalar2(1)
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
