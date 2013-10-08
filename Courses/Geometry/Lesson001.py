'''
The first thing we will do is create a linear space, axiom by axiom.
Our space will have two kinds of elements we call vectors and scalars.
With an eye to creating a unified geometric space, the underlying object is a Euclidean.
We demonstrate that the objects f,g, and k are elements in the space.
'''
class Euclidean:
    def __init__(self, w, x, y):
        self.w = w
        self.x = x
        self.y = y
    
#    def __str__(self):
#        return "[]"
    
    def __repr__(self):
        return "Euclidean(" + str(self.w) + str(self.x) + str(self.y) + ")"

def Vector(x, y):
    return Euclidean(0, x, y)

def Scalar(w):
    return Euclidean(w, 0, 0)

f = Vector(1,2)
g = Vector(3,5)
k = Scalar(4)

# It's not possible to distinguish scalars from vectors yet.
# At least we can see that they are all the same type.
print "f : " + repr(f)
print "g : " + repr(g)
print "k : " + repr(k)
