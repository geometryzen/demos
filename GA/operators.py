from e3ga import *
from random import *
from units import *

e1 = VectorE3(1,0,0)
e2 = VectorE3(0,1,0)
e3 = VectorE3(0,0,1)

a = (random() * e1 + random() * e2 + random() * e3) * meter
b = (random() * e1 + random() * e2 + random() * e3) * meter
c = (random() * e1 + random() * e2 + random() * e3) * meter

print a * b
print a | b + a ^ b
print a << b + a ^ b
print a >> b + a ^ b
print
print a * b | c
print a * (b | c)