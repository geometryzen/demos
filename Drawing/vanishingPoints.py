from browser import *;
from workbench import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

popUp = window.open("","","width=%s, height=%s" % (WINDOW_WIDTH, WINDOW_HEIGHT))

def tick(t):
    pass

def terminate(t):
    return False

def setUp():
    pass

def tearDown(e):
    popUp.close()
    if e:
        print e

war = WindowAnimationRunner(tick, terminate, setUp, tearDown)
war.start()
