from cmath import *
from e2ga import *

z = complex(3,4)
v = VectorE2(12,13)

print z
print v
try:
    print v * z
except TypeError as e:
    print e

print z * v