# Under Construction 2013-Jul-07
from eight import *
print "Quaternions"
print "----------"
print "Construction"
print "----------"
quaternion = Quaternion(1, 2, 3, 4)
print repr(quaternion)
print str(quaternion)
print "quaternion.x => " + str(quaternion.x)
print "quaternion.y => " + str(quaternion.y)
print "quaternion.z => " + str(quaternion.z)
print "quaternion.w => " + str(quaternion.w)

print "----------"
print "Defaults for Quaternion()"
print "----------"
print repr(Quaternion())
print str(Quaternion())
print "x => " + str(Quaternion().x)
print "y => " + str(Quaternion().y)
print "z => " + str(Quaternion().z)
print "w => " + str(Quaternion().w)
print "----------"
print "Assignment"
print "----------"
quaternion = Quaternion(0,0,0,0)
print repr(quaternion)
print str(quaternion)
quaternion.x = 1
quaternion.y = 2
quaternion.z = 3
quaternion.w = 4
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
print target.setFromEuler(vector)
print repr(target)
