# Geometry.py
from three import *

geometry = Geometry()
print str(geometry)
print repr(geometry)
print str(type(geometry))
print repr(type(geometry))

vs = geometry.vertices
print vs
vs.append(Vector3(0,0,0))
print vs

