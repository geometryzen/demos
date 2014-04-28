from math import *
from units import *
from cmath import *
from e2ga import *
from e3ga import *
'''
Quadrance is a term introduced by NJ Wildberger.
'''

print quadrance(2)
print quadrance(2.0)

try:
    print quadrance('Hello')
except Exception as e:
    print e
    pass

z = complex(3.0,4.0)
print z
print quadrance(z)
print sqrt(quadrance(z))

r = Euclidean2(4,3,2,1)
print r
print quadrance(r)
