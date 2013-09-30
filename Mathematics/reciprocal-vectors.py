'''
Reciprocal vectors in two dimensions.

The purpose is to show that we can construct reciprocal vectors using geometric algebra.
Note that the cross-product construction in 3 dimensions 
'''
from e2ga import *
from e3ga import *

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


i = VectorE3(1, 0, 0)
j = VectorE3(0, 1, 0)
k = VectorE3(0, 0, 1)
e1 = 12 * i
e2 = 3 * i + 4 * j
e3 = k
v = (e1.cross(e2)) % e3
r1 = e2.cross(e3) / v
r2 = e3.cross(e1) / v

print r1 << e1
print r1 << e2
print r2 << e1
print r2 << e2
