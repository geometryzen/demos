from e2ga import *

def explain(m):
    print str(m) + " is " + repr(m)
    return m

def showValue(name, x):
    print name + " => " + str(x)
    return x

i = Vector2(1,0)
j = Vector2(0,1)
x = Vector2(0,0)
I = Pseudoscalar2(1)
explain(i)
explain(j)
explain(x)

x = i * j
showValue("x", x)
showValue("+x", +x)
showValue("-x", -x)
showValue("~x", ~x)
