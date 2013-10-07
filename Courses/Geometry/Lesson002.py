'''

'''
class Euclidean:
    def __init__(self):
        pass
    
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
print "f : " + repr(f)
print "g : " + repr(g)
print "f + g : " + repr(f + g)
