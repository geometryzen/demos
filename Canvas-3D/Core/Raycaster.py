from browser import window
from three import *

THREE = window.THREE

origin = VectorE3(1.0, 0.0, 0.0)
direction = VectorE3(1.0, 0.0, 0.0, False)
near = 0.01
far = 10000.0

raycaster = Raycaster(origin, direction, near, far)

print raycaster.ray
print raycaster.near
print raycaster.far

print raycaster
print repr(raycaster)