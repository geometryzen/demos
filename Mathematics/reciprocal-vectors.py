'''
Reciprocal vectors in two dimensions
'''
from e2ga import *

i = VectorE2(1, 0)
j = VectorE2(0, 1)
e1 = 12 * i
e2 = 3 * i + 4 * j
r1 = e2 / (e1 ^ e2)
r2 = -e1 / (e1 ^ e2)

print r1 << e1
print r1 << e2
print r2 << e1
print r2 << e2

s = e2 - (e << e1) * e1 / (e1 * e1)

print s
