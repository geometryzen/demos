from browser import *;

WINDOW_WIDTH  = 800
WINDOW_HEIGHT = 800
CANVAS_HEIGHT = 800
CANVAS_WIDTH  = 800

popUp = window.open("","","width=%s, height=%s" % (WINDOW_WIDTH, WINDOW_HEIGHT))

def tick(t):
    pass

def terminate(t):
    return False

def setUp():
    popDoc = popUp.document
    canvas = popDoc.createElement("canvas")
    
    canvas.setAttribute("id", "graph")
    canvas.setAttribute("width", str(CANVAS_WIDTH))
    canvas.setAttribute("height",str(CANVAS_HEIGHT))

def tearDown(e):
    popUp.close()
    if e:
        print e

war = WindowAnimationRunner(tick, terminate, setUp, tearDown, popUp)
war.start()
