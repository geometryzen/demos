from e3ga import *
from random import *
from units import *

e1 = VectorE3(1,0,0)
e2 = VectorE3(0,1,0)
e3 = VectorE3(0,0,1)

a = (2 * e1 + 3 * e2 + 5 * e3)
b = (7 * e1 + 11 * e2 + 13 * e3)
c = (17 * e1 + 19 * e2 + 23 * e3)

print a
print b
print a * b
print a | b + a ^ b
print a << b + a ^ b
print a >> b + a ^ b
print
print a * b | c
print a * (b | c)
