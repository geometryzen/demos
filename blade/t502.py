from eight import *

def explain(m):
    print str(m) + " is " + repr(m)
    return m

def showValue(name, m):
    print name + " => " + str(m)
    return m

zero  = Scalar3(0)
one   = Scalar3(1)
two   = Scalar3(2)
three = 3
i     = Vector3(1, 0, 0)
j     = Vector3(0, 1, 0)
k     = Vector3(0, 0, 1)
ij    = Bivector3(1, 0, 0)
jk    = Bivector3(0, 1, 0)
ki    = Bivector3(0, 0, 1)
I     = Pseudoscalar3(1, 0, 0)

blades = [zero, one, two, three, i, j, k, ij, jk, ki, I]

sum = one + i + j + k + ij + jk + ki + I

print "----------"
print "repr"
print "----------"
print repr(zero)
print repr(one)
print repr(two)
print repr(three)
print repr(i)
print repr(j)
print repr(k)
print repr(ij)
print repr(jk)
print repr(ki)
print repr(I)
print "----------"
print "str"
print "----------"
print str(zero)
print str(one)
print str(two)
print str(three)
print str(i)
print str(j)
print str(k)
print str(ij)
print str(jk)
print str(ki)
print str(I)
print "----------"
print "Addition +"
print "----------"
for a in blades:
    for b in blades:
        showValue(str(a) + " + " + str(b), a + b)
    print ""
print "----------"
print "Subtraction -"
print "----------"
for a in blades:
    for b in blades:
        showValue(str(a) + " - " + str(b), a - b)
    print ""
print "----------"
print "Multiplication *"
print "----------"
for a in blades:
    for b in blades:
        showValue(str(a) + " * " + str(b), a * b)
    print ""
print "----------"
print "Extension ^"
print "----------"
for a in blades:
    for b in blades:
        showValue(str(a) + " ^ " + str(b), a ^ b)
    print ""



