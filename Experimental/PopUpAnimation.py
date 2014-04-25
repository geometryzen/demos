from browser import *
from math import *

win = window.open("","","width=415,height=400")

def tick(time):
    pass

def terminate(time):
    pass

def setUp():
    pass

def tearDown():
    pass

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()

win.close()
