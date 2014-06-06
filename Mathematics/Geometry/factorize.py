# Factorizing a Blade using the contraction and a random seed vector.
from e3ga import *
from math import *
from random import *

e1 = VectorE3(1,0,0)
e2 = VectorE3(0,1,0)
e3 = VectorE3(0,0,1)

B = VectorE3(random(),random(),random()) ^ VectorE3(random(),random(),random()) ^ VectorE3(random(),random(),random())
B = e1 ^ e2 ^ e3

print B

x = VectorE3(random(),random(),random())
x = x / magnitude(x)
x = e1

a = x << B
a = a / magnitude(a)

b = a << B

print a ^ b

print a
print b
