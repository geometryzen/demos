from e3ga import *
from random import random

i = VectorE3(1,0,0)
j = VectorE3(0,1,0)
k = VectorE3(0,0,1)
I = i * j * k

a = 5 * i + 3 * j + 2 * k
b = 7 * i + 4 * j + 9 * k
c = random() * i + 5 * j + 16 * k

print a.dot(b.cross(c))
print a ^ b ^ c
print a.dot(-I * (b^c))