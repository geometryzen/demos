# The quaternions are isomorphic to the even sub-algebra of Euclidean Space (e3ga).
# TODO: division; Quaternions are after all a division algebra! 
from three import *
from math import pi

def showValue(name, m):
    print name + " => " + str(m)
    return m

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
print "setFromAxisAngle(axis, angle) Quaternion"
print "----------"
axis = Vector3(1.0, 1.0, 1.0).normalize()
target = Quaternion()
print target.setFromAxisAngle(axis, pi/2)
print repr(target)
print "----------"
print "inverse()"
print "----------"
print Quaternion(4, 3, 2, 1).inverse()
print Quaternion(4, 3, 2, 1) * Quaternion(4, 3, 2, 1).inverse()
print "----------"
print "length()"
print "----------"
source = Quaternion(4, 3, 2, 1)
print source.length()
print "----------"
print "lengthSq()"
print "----------"
source = Quaternion(4, 3, 2, 1)
print source.lengthSq()
print "----------"
print "normalize()"
print "----------"
source = Quaternion(4, 3, 2, 1)
print source.normalize()
print "----------"
print "clone()"
print "----------"
source = Quaternion(4, 3, 2, 1)
print source.clone()
print "----------"
print "operators"
print "----------"
one = Quaternion(0, 0, 0, 1)
i   = Quaternion(1, 0, 0, 0)
j   = Quaternion(0, 1, 0, 0)
k   = Quaternion(0, 0, 1, 0)
qs = [one, i, j, k]
print "----------"
print "Addition +"
print "----------"
for a in qs:
    for b in qs:
        showValue(str(a) + " + " + str(b), a + b)
    print ""
print "----------"
print "Subtraction -"
print "----------"
for a in qs:
    for b in qs:
        showValue(str(a) + " - " + str(b), a - b)
    print ""
print "----------"
print "Multiplication *"
print "----------"
for a in qs:
    for b in qs:
        showValue(str(a) + " * " + str(b), a * b)
    print ""
