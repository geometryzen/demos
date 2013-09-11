from three import *

def showValue(name, m):
    print name + " => " + str(m)
    return m

e1 = Vector3(1, 0, 0)
e2 = Vector3(0, 1, 0)
e3 = Vector3(0, 0, 1)

q1 = Quaternion(5, 0, 0, 12).normalize()
q2 = Quaternion(0, 1, 0, 1).normalize()
q3 = Quaternion(0, 0, 1, 1).normalize()

print q1
print q2
print q3

es = [e1, e2, e3]
qs = [q1, q2, q3]

for e in es:
    for q in qs:
        showValue(str(e) + " applyQuaternion " + str(q), e.clone().applyQuaternion(q))
    print ""
