from three import *

class Bird(Object3D):
    def __init__(self):
        pass
    
    def __str__(self):
        return "Birdie"
        pass
    
    
b = Bird()
b.velocity = VectorE3(1,2,3)
print b.velocity
print repr(b)
