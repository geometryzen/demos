from three import *

# TODO: Implement Euler wrapper.
a = Euler(0, 1, 1.57, 'XYZ')
b = Vector3(1, 0, 1)
c = b.sub(a)

print c.x
print c.y
print c.z