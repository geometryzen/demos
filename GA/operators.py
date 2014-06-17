from e3ga import *
from random import *

e1 = VectorE3(1,0,0)
e2 = VectorE3(0,1,0)
e3 = VectorE3(0,0,1)

print e1
print e2
print e3

a = random() * e1 + random() * e2 + random() * e3
b = random() * e1 + random() * e2 + random() * e3

print a
print b

print a * b
print a % b + a ^ b
print a << b + a ^ b
print a >> b + a ^ b
print a << b
print a >> b
#print a | b
