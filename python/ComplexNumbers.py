# Complex Numbers
from cmath import *

z = complex(11.0, 7.0)
w = complex(5, 3)

print z.real
print z.imag
print "----------"
print z
print str(z)
print repr(z)
print "----------"
print z + w
print z - w
print z * w
print z / w
print "----------"
print z == z
print z != z
print z == w
print z != w
print "----------"
print phase(complex(-1.0, 0.0))
print phase(z)
print type(1.0)
print type(z)(1.0,3)
print type(z)
print str(type(z))
print repr(type(z))
