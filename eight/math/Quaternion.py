# Under Construction 2013-Jul-07
# Quaternion.py
from eight import *

print "----------"
print "Construction"
print "----------"
quaternion = Quaternion(1,2,3,4)
print quaternion
print str(quaternion)
print repr(quaternion)
print "quaternion.x => " + str(quaternion.x)
print "quaternion.y => " + str(quaternion.y)
print "quaternion.z => " + str(quaternion.z)
print "quaternion.w => " + str(quaternion.w)

print "----------"
print "Defaults"
print "----------"
print Quaternion()
print repr(Quaternion())
print "x => " + str(Quaternion().x)
print "y => " + str(Quaternion().y)
print "z => " + str(Quaternion().z)
print "w => " + str(Quaternion().w)
print "----------"
print "Assignment"
print "----------"
quaternion = Quaternion(0,0,0,0)
print quaternion
print str(quaternion)
print repr(quaternion)
quaternion.x = 10
quaternion.y = 20
quaternion.z = 30
quaternion.w = 40
print quaternion
print str(quaternion)
print repr(quaternion)
print "----------"
print "set(x, y, z, w)"
print "----------"
print repr(quaternion.set(17,13,11,7))
print "quaternion.x => " + str(quaternion.x)
print "quaternion.y => " + str(quaternion.y)
print "quaternion.z => " + str(quaternion.z)
print "quaternion.w => " + str(quaternion.w)
print "----------"
print "copy(q) Quaternion"
print "----------"
target = Quaternion()
source = Quaternion(4, 3, 2, 1)
print target.copy(source)
print repr(target)
print "----------"
print "setFromEuler(vector) Quaternion"
print "----------"
vector = Vector3(0.5, 1.0, 2.0)
target = Quaternion()
#print target.setFromEuler(vector)
print repr(target)
