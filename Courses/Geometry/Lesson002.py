'''

'''
class Euclidean:
    def __init__(self):
        pass
    
    def __add__(self, other):
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

# We want f + g to be in the vector space.
# Python allows us to do this using __add__.
print "f : " + repr(f)
print "g : " + repr(g)
print "f + g : " + repr(f + g)
