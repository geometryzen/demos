from e3ga import *
from units import *
from math import *

e1 = VectorE3(1,0,0) * dimensionless
e2 = VectorE3(0,1,0) * dimensionless
e3 = VectorE3(0,0,1) * dimensionless
r  = (4 * e1 + 3 * e2 + 2 * e3) * meter

print r
print magnitude(r)
print abs(r)

# Using the % symbol means scalar product.
print e1 % e2

print e1 ^ e2

print (e1 * meter) ^ (e2 * meter)
print (e1 * meter) % (e2 * meter)

print "r_x = %s" % str((r % e1) * e1)