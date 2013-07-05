# MultiVector3 demonstration of Euclidean 3D Geometric Algebra.
from eight import *

def explain(m):
    print str(m) + " is " + repr(m)
    return m

def showValue(name, m):
    print name + " => " + str(m)
    return m

zero = explain(Euclidean3(0, 0, 0, 0, 0, 0, 0, 0))
one = explain(Scalar3(1))
two = explain(Scalar3(2))
three = explain(3)
e1 = explain(Vector3(1, 0, 0))
e2 = explain(Vector3(0, 1, 0))
e3 = explain(Vector3(0, 0, 1))
e12 = explain(Bivector3(1, 0, 0))
e23 = explain(Bivector3(0, 1, 0))
e31 = explain(Bivector3(0, 0, 1))
I = explain(Pseudoscalar3(1))

blades = [zero, one, two, three, e1, e2, e3, e12, e23, e31, I]

# Skulpt bug? The string representation of the list does not recurse.
# print str(blades)

# addition uses the + operator, as you would expect.
sum = showValue("sum", one + e1 + e2 + e3 + e12 + e23 + e31 + I)

# grade extraction is performed using Python's indexing operator [].
print ""
print "Grade extraction operator []"
print "============================"
for grade in range(0, 4):
    showValue("sum[" + str(grade) + "]", sum[grade])

# subtraction uses the - operator, as you would expect.
showValue("zero + sum", zero + sum)
showValue("0 + sum", 0 + sum)

showValue("zero - sum", zero - sum)
showValue("0 - sum", 0 - sum)

showValue("one * sum", one * sum)
showValue("1 * sum", 1 * sum)

showValue("one ^ sum", one ^ sum)
showValue("1 ^ sum", 1 ^ sum)
print ""
print "Geometric Product Table *"
print "========================="
for a in blades:
    for b in blades:
        showValue(str(a) + " * " + str(b), a * b)
    print ""
print ""
print "Exterior Product Table *"
print "========================="
for a in blades:
    for b in blades:
        showValue(str(a) + " ^ " + str(b), a ^ b)
    print ""
print ""
print "Left Contraction Product Table <<"
print "================================="
for a in blades:
    for b in blades:
        showValue(str(a) + " << " + str(b), a << b)
    print ""
    print ""
print "Right Contraction Product Table >>"
print "=================================="
for a in blades:
    for b in blades:
        showValue(str(a) + " >> " + str(b), a >> b)
    print ""