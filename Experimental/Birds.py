from three import *

class Bird(Object3D):
    def __init__(self):
        pass
    
    def __str__(self):
        return "Birdie"
        pass
    
    
b = Bird()

print b
print repr(b)
