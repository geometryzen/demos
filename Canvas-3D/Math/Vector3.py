from three import *

a = Vector3(1,1,1)

print str(a)
print repr(a)
print type(a)

a.x = 7
a.y = 6
a.z = 5
print a
print "a.x   => " + str(a.x)
print "a.y   => " + str(a.y)
print "a.z   => " + str(a.z)

# The string value of the zero vector is just "0"
print "str(Vector3(0,0,0)) => " + str(Vector3(0,0,0))
print "repr(Vector3(0,0,0)) => " + repr(Vector3(0,0,0))

# The constructor without arguments gives the zero vector:
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
print a.magnitude()
print a.normalize()
print a
print a.magnitude()

# Linear Algebra
i = Vector3(1,0,0)
j = Vector3(0,1,0)
k = Vector3(0,0,1)
print i
print j
print k
print i + j
print i - j
print i * 2.0
print 2.0 * i
print i + j - k
print i - j + k
