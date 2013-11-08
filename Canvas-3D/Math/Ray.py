from three import *

origin = VectorE3(1.0, 2.0, 3.0)
direction = e3

ray = Ray(origin, direction)

print ray.origin
print ray.direction

print ray
print repr(ray)