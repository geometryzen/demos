from three import *

origin = VectorE3(1.0, 2.0, 3.0)
direction = VectorE3(0.0, 0.0, 1.0)

ray = Ray(origin, direction)

print ray.origin
print ray.direction

print ray
print repr(ray)