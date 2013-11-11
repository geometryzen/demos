'''
Under construction. Nov 11, 2013.
'''
from three import *
from e3ga import *

class Reptile():
    def __init__(self):
        pass
    
    def talk(self):
        pass

class Bird(Geometry):
    def __init__(self):
        pass
    
    def __str__(self):
        return "Birdie"
        pass
    
    
b = Bird()

b.pqr = VectorE3(1,2,3)

print b.pqr

print repr(b)
