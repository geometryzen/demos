# Geometry demonstration.
from three import *

geometry = Geometry()
print str(geometry)
print repr(geometry)
print str(type(geometry))
print repr(type(geometry))

vs = geometry.vertices
print vs
vs.append(Vector3(0,0,0))
vs.append(Vector3(60,0,0))
print vs
print vs[0]
print vs[1]
print geometry.vertices

