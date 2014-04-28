from math import *
from units import *
from cmath import *
from e3ga import *
'''
Quadrance is a term introduced by NJ Wildberger.
'''

print magnitude(2.0)
print abs(-2)
print quadrance(2)
print quadrance(2.0)
print sqrt(2)

try:
    print quadrance('Hello')
except Exception as e:
    print e
    pass

z = complex(3.0,4.0)
print z
print quadrance(z)
print sqrt(quadrance(z))
print magnitude(z)

r = VectorE3(3,4,12)
print r
print quadrance(r)
print sqrt(quadrance(r))


r = VectorE3(4,3,2) * meter
print r
print quadrance(r)
print sqrt(quadrance(r))
print magnitude(r)
print abs(r)
