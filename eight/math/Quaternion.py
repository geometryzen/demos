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
