from e3ga import *
from units import *

e1 = VectorE3(1,0,0) * dimensionless
e2 = VectorE3(0,1,0) * dimensionless
r = VectorE3(4,3,2) * meter

print r

# Using the % symbol means scalar product.
print e1 % e2

print e1 ^ e2

print (e1 * meter) ^ (e2 * meter)
print (e1 * meter) % (e2 * meter)

print "\\[r_x\\] = %s" % str((r % e1) * e1)