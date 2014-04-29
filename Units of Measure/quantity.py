from cmath import *
from e2ga import *
from e3ga import *

z = complex(3,4)
v = VectorE2(12,13)
x = VectorE3(1,0,0)

print z
print v
try:
    print v * z
except TypeError as e:
    print e

try:
    print z * v
except TypeError as e:
    print e
