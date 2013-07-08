# Quaternion.py
from eight import *

quaternion = Quaternion(1,2,3,4)
print quaternion
print str(quaternion)
print repr(quaternion)
print "quaternion.x => " + str(quaternion.x)
print "quaternion.y => " + str(quaternion.y)
print "quaternion.z => " + str(quaternion.z)
print "quaternion.w => " + str(quaternion.w)

print Quaternion()
print repr(Quaternion())