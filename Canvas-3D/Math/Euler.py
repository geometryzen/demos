from three import *

# TODO: Implement Euler wrapper.
a = Euler(0, 1, 1.57, 'XYZ')
b = Vector3(1, 0, 1)
c = b.applyEuler(a)

print c.x
print c.y
print c.z

print a.x
print a.y
print a.z
print a.order
print a
print str(a)
print repr(a)

a.set(1,2,3,'ZXY')