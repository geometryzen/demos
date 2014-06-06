from e3ga import *
from math import *
from random import *

e1 = VectorE3(1,0,0)
e2 = VectorE3(0,1,0)
e3 = VectorE3(0,0,1)

B = e1 ^ e2

print B

x = VectorE3(random(),random(),random())

print x

a = x << B

print a
print magnitude(a)

b = y << B

print b


