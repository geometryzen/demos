from three import *

e1 = Vector3(1, 0, 0)
e2 = Vector3(0, 1, 0)
e3 = Vector3(0, 0, 1)

q1 = Quaternion(1, 0, 0, 1).normalize()
q2 = Quaternion(0, 1, 0, 1).normalize()
q3 = Quaternion(0, 0, 1, 1).normalize()

print q1
print q2
print q3

print e1.applyQuaternion(q1)
print e1.applyQuaternion(q2)
