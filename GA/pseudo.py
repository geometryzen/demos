from e3ga import *
from random import random

i = VectorE3(1,0,0)
j = VectorE3(0,1,0)
k = VectorE3(0,0,1)
I3 = i * j * k

a = random() * i + random() * j + random() * k
b = random() * i + random() * j + random() * k
c = random() * i + random() * j + random() * k

print a.dot(b.cross(c))
print a ^ b ^ c
print a.dot(-I3 * (b^c))