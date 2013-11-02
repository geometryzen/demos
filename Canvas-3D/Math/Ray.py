from three import *

origin = VectorE3(1,2,3)
direction = e3

ray = Ray(origin, direction)

print ray.origin
print ray.direction

print ray
print repr(ray)