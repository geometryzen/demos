from units import *
from e2ga import *

e1 = VectorE2(1,0)
e2 = VectorE2(0,1)

print "e1 => %s" % e1
print "e2 => %s" % e2

x = VectorE2(3,4) * meter

print "x => %s" % x

try:
    print e1 + x
except TypeError as e:
    print e

try:
    print x + e1
except TypeError as e:
    print e
    
print "e1 * x => %s" % (e1 * x)
print "x * e1 => %s" % (x * e1)
print "e1 ^ x => %s" % (e1 ^ x)
print "x ^ e1 => %s" % (x ^ e1)
