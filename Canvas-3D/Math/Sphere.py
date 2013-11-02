from three import *

center = VectorE3(1, 2, 3)
radius = 1.0

sphere = Sphere(center, radius)

print sphere.center
print sphere.radius

print sphere
print repr(sphere)

s1 = Sphere(VectorE3(0, 0, 0), 0.1)
s2 = Sphere(VectorE3(2, 2, 2), 1.5)

print sphere.intersectsSphere(sphere)
print s1.intersectsSphere(s2)

print Sphere().copy(s2)

print s1.distanceToPoint(VectorE3(1, 0, 0))