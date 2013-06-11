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

print "1 * 1 = " + str(one * one)
print "1 * i = " + str(one * i)
print "1 * j = " + str(one * j)
print "1 * I = " + str(one * I)

print "i * 1 = " + str(i * one)
print "i * i = " + str(i * i)
print "i * j = " + str(i * j)
print "i * I = " + str(i * I)

print "j * 1 = " + str(j * one)
print "j * i = " + str(j * i)
print "j * j = " + str(j * j)
print "j * I = " + str(j * I)
