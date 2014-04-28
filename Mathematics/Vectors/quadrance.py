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
    print quadrance("Hello")
except Exception as e:
    print e
    pass

c = complex(3.0,4.0)
print str(c)
print repr(c)
print type(c)
print meter
print str(meter)
print type(meter)
print str(type(meter))
print type(type(meter))
q = quadrance(VectorE3(1,0,0))
print q
m = sqrt(q)
