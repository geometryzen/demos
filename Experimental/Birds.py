from three import *

class Bird(Geometry):
    def __init__(self, more):
        print more
        pass
    
    def __str__(self):
        return "Birdie"
        pass
    
    
b = Bird()

print b
print repr(b)
