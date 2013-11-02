'''
Under construction. Nov 2, 2013
'''
from three import *

center = VectorE3(1,2,3)
radius = 1.0

sphere = Sphere(center, radius)

print sphere.center
print sphere.radius

print sphere
print repr(sphere)

print sphere.intersectsSphere(sphere)