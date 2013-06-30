# Vector3 demonstration.
from eight import *

a = Vector3(1,1,1)

print str(a)
print repr(a)
print str(type(a))
print repr(type(a))

#
# It is important to realize that MultiVector3 is mutable.
# This contrasts to the usual approach of treating mathematical
# objects as immutable types. The reason for this is that MultiVector3
# is part of a graphics library that deals with mutable
# objects for performance.
a.w = 8
a.x = 7
a.y = 6
a.z = 5
a.xy = 4
a.yz = 3
a.zx = 2
a.xyz = 1
print a
print "a.w   => " + str(a.w)
print "a.x   => " + str(a.x)
print "a.y   => " + str(a.y)
print "a.z   => " + str(a.z)
print "a.xy  => " + str(a.xy)
print "a.yz  => " + str(a.yz)
print "a.zx  => " + str(a.zx)
print "a.xyz => " + str(a.xyz)

# The string value of the zero vector is just "0"
print "str(Vector3(0,0,0)) => " + str(Vector3(0,0,0))
print "repr(Vector3(0,0,0)) => " + repr(Vector3(0,0,0))

# The constructor without arguments gives the zero multivector:
print "Vector3() => " + str(Vector3())

# The setX, setY and setZ methods are chainable.
a = Vector3().setX(4).setY(7).setZ(9)
print a

# setComponent(index, value) and getComponent(index)
a.setComponent(0, 4.4)
a.setComponent(1, 7.7)
a.setComponent(2, 9.9)
print a

print a.getComponent(0)
print a.getComponent(1)
print a.getComponent(2)

print a.set(3,5,7)
print a

b = a.clone()
a.set(4,7,9)
print b
print a
print a.length()
print a.normalize()
print a
print a.length()

# Linear Algebra
i = Vector3(1,0,0)
j = Vector3(0,1,0)
k = Vector3(0,0,1)
print i
print j
print k
print i + j
print i + 3
print 3 + i
print a * 2.0
print 2.0 * a
print i + j - k
print i - j + k
