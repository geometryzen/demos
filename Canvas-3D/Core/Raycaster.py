'''
Under Construction. Nov 2, 2013
'''
from three import *

origin = VectorE3(1,0,0)
direction = e1
near = 0.01
far = 10000.0

raycaster = Raycaster(origin, direction, near, far)

print raycaster.near
print raycaster.far

print raycaster
print repr(raycaster)