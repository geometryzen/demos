# Complex Numbers
from cmath import *

z1 = complex(11.0, 7.0)
z2 = complex(5, 3)

print z1.real
print z1.imag
print "----------"
print z1
print str(z1)
print repr(z1)
print "----------"
print z1 + z2
print z1 - z2
print z1 * z2
print z1 / z2
print "----------"
print z1 == z1
print z1 != z1
print z1 == z2
print z1 != z2
print "----------"
print phase(complex(-1.0, 0.0))
print phase(z1)
print type(z1)
