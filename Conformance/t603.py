from e3ga import *

def explain(m):
    print str(m) + " is " + repr(m)
    return m

def showValue(name, m):
    print name + " => " + str(m)
    return m

zero  = ScalarE3(0.0)
one   = ScalarE3(1.0)
two   = ScalarE3(2.0)
i     = VectorE3(1.0, 0.0, 0.0)
j     = VectorE3(0.0, 1.0, 0.0)
k     = VectorE3(0.0, 0.0, 1.0)
ij    = BivectorE3(1.0, 0.0, 0.0)
jk    = BivectorE3(0.0, 1.0, 0.0)
ki    = BivectorE3(0.0, 0.0, 1.0)
I     = PseudoscalarE3(1.0)

blades = [zero, one, two, i, j, k, ij, jk, ki, I]

sum = one + i + j + k + ij + jk + ki + I

print "----------"
print "repr"
print "----------"
print repr(zero)
print repr(one)
print repr(two)
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
print "----------"
print "Left Contraction <<"
print "----------"
for a in blades:
    for b in blades:
        showValue(str(a) + " << " + str(b), a << b)
    print ""
print "----------"
print "Right Contraction >>"
print "----------"
for a in blades:
    for b in blades:
        showValue(str(a) + " >> " + str(b), a >> b)
    print ""
