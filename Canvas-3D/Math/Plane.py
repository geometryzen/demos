from three import *

normal = VectorE3(0.0, 0.0, 1.0)
offset = 1.0

plane = Plane(normal, offset)

print plane.normal
print plane.offset

print plane
print repr(plane)

s1 = Plane(VectorE3(0.0, 0.0, 0.0), 0.1)
s2 = Plane(VectorE3(2.0, 2.0, 2.0), 1.5)
