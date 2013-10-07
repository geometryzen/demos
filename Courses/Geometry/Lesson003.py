'''
A linear space, V, is a set endowed with a rule for addition.
If f and g are in V, then so is f + g.
There is also a rule for scalar mutiplication.
If f is in V and k is a scalar, then kf is in V.
'''
class Euclidean:
    def __init__(self):
        pass
    
    def __add__(self, other):
        return Euclidean()

    def __mul__(self, other):
        return Euclidean()
    
    def __repr__(self):
        return "Euclidean()"

def Vector():
    return Euclidean()

def Scalar():
    return Euclidean()

f = Vector()
g = Vector()
k = Scalar()

# We want f + g to be in the vector space (a Euclidean vector).
# Python allows us to do this using __add__.
print "f : " + repr(f)
print "g : " + repr(g)
print "f + g : " + repr(f + g)
print "f * g : " + repr(f * g)
