'''
Under Construction. Nov 3, 2013
'''
from three import *

normal = VectorE3(0, 0, 1)
offset = 1.0

plane = Plane(normal, offset)

print plane.normal
print plane.offset

print plane
print repr(plane)

s1 = Plane(VectorE3(0, 0, 0), 0.1)
s2 = Plane(VectorE3(2, 2, 2), 1.5)
