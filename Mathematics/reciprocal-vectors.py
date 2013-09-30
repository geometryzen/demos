'''
Reciprocal vectors in two dimensions
'''
from e2ga import *

i = VectorE2(1, 0)
j = VectorE2(0, 1)
e1 = 12 * i
e2 = 3 * i + 4 * j
print e1 ^ e2
