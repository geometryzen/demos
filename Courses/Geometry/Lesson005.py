'''
A linear space, V, is a set endowed with a rule for addition.
If f and g are in V, then so is f + g.
There is also a rule for scalar mutiplication.
If f is in V and k is a scalar, then kf is in V.
For al f,g,h in V and c,k scalars, the set also satisfies the following rules:
1. (f + g) + h = f + (g + h)
2. f + g = g + f
3. There exists a neutral element n in V such that f + n = f, for al f in V.
This n is unique and denoted by 0.
'''
class Euclidean:
    def __init__(self):
        pass
    
    def __add__(self, other):
        return Euclidean()

    def __mul__(self, other):
        return Euclidean()
    
    def __eq__(self, other):
        return True
    
    def __repr__(self):
        return "Euclidean()"

def Vector():
    return Euclidean()

def Scalar():
    return Euclidean()

f = Vector()
g = Vector()
h = Vector()
k = Scalar()
n = Vector()

print "f : " + repr(f)
print "g : " + repr(g)
print "f + g : " + repr(f + g)
print "k * f : " + repr(k * f)
print (f + g) + h == f + (g + h)
print f + g == g + f
print f + n == f
print n != f
