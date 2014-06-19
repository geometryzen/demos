from units import *
from e3ga import *

e1 = VectorE3(1,0,0)
e2 = VectorE3(0,1,0)

print "e1 => %s" % e1
print "e2 => %s" % e2

x = VectorE3(3,4,5) * meter

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
print "e1 mod x => %s" % (e1 | x)
print "x mod e1 => %s" % (x | e1)
print "e1 << x => %s" % (e1 << x)
print "x << e1 => %s" % (x << e1)
print "e1 >> x => %s" % (e1 >> x)
print "x >> e1 => %s" % (x >> e1)
