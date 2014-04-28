from math import *
from units import *
from cmath import *
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

c = complex(-3.0,0.0)
print c
print quadrance(c)
print sqrt(quadrance(c))
